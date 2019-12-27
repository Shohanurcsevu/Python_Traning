import smtplib
sender= input()
receivers = input()

message =' Power of python shown to you'

try:
    smtpobj=smtplib.SMTP('localhost')
    smtpobj.login('joti7569@gmail.com','shohan@shajuty')
    smtpobj.sendmail(sender,receivers,message)
    print("Succesfully Send")

except BaseException:
    print()
