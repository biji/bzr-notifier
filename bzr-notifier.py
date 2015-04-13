
import os
import subprocess
import smtplib
import email.utils

########## CONFIGURATION ########## 
path = '/x/'
sender = "noreply@domain.com"
recipients = ["dev2@domain.com"]
smtp_host = "localhost" 
########## END CONFIGURATION ######


dirs = os.listdir( path )

for dir1 in dirs:
	branch = os.path.join(path, dir1)
	if os.path.isdir( branch ):
		if os.path.isfile( os.path.join(branch, ".bzr/branch/branch.conf") ):
			revno = subprocess.check_output(["bzr","revno",branch]).strip()
			revno = int(float( revno ))

			print ("Found branch: %s (revno: %d)" %(branch,revno))

			conf = os.path.join(branch, ".bzr/branch/bzr-notifier.txt")
			last_sent = 0
			if os.path.isfile( conf ):
				with file(conf) as f:
					s = f.read().strip()
					try:
						last_sent = int(float(s))
					except:
						pass
			#print "Last sent: %d" % last_sent

			
			if last_sent < revno:
				# send email
				email_subject = branch + " revno " + subprocess.check_output(["bzr","log","-l1","--line",branch]).strip()
				email_body = subprocess.check_output(["bzr","log","-l1","-v",branch])
				email_date = email.utils.formatdate(localtime=True)

				#print email_subject
				#print email_body

				message = """From: %s
To: %s
Subject: %s
Date: %s

%s""" % (sender, ', '.join(recipients), email_subject, email_date, email_body)	

				#print message

				try:
					smtpo = smtplib.SMTP(smtp_host)
					smtpo.sendmail(sender, recipients, message)

					#save last_sent
					f = open(conf,'w')
					f.write( "%d" % revno )
					f.close()

				except:
					print "Error: unable to send email"


