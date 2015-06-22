import sys
import smtplib
#usage: python sendmail.py recv_email subject message_in_file your_email your_email_password
#gmail: the below are from https://support.google.com/accounts/answer/6010255?hl=en
#Go to Allow less secure apps https://www.google.com/settings/security/lesssecureapps and choose "Allow" to let less secure apps access your Google account.
#We don't recommend this option because it may make it easier for someone to gain access to your account.
if __name__ == '__main__':
	smtpdomain = sys.argv[4].split('@')[-1]
	print 'connecting to smtp.'+ smtpdomain + '...'
	mail = smtplib.SMTP('smtp.' + smtpdomain, 587)
	print 'connected to stmp.'+ smtpdomain + '...'
	mail.ehlo()
	mail.starttls()
	print 'tls started...'
	mail.login(sys.argv[4], sys.argv[5])
	print 'logged in as: ' + sys.argv[4].split('@')[0]
	with open (sys.argv[3], "r") as myfile:
		data=myfile.read()
		message = 'Subject: %s\n\n%s' % (sys.argv[2], data)
		mail.sendmail(sys.argv[3], sys.argv[1], message)
		print 'sending email with subject: '+ sys.argv[2] +' to: ' + sys.argv[1]
		print 'content from file: ' + sys.argv[3]
		print 'message:\n' + data[:100] + '...'
	mail.close()
	print 'finished!'
