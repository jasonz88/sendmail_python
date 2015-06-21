import sys
import smtplib
def sendemail(recv, content):
	mail = smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
	mail.starttls()
	mail.login('nvtester88@gmail.com','nvidia3d')
	with open (content, "r") as myfile:
		data=myfile.read()
		mail.sendmail('nvtester88@gmail.com',recv,data)
	mail.close()
if __name__ == '__main__':
	sendemail(sys.argv[1],sys.argv[2])

