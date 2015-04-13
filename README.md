# bzr-notifier
Server side email notifier for bazaar. 
Will create last email sent revno in .bzr/branch/bzr-notifier.txt

To setup:

1. Copy the script to bazaar server
2. Edit configuration on top of script
3. Create crontab like this: */5 * * * * python /x/bzr-notifier.py
4. Setup postfix at localhost (optional)

