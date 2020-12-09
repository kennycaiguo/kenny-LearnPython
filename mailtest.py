import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host ="smtp.gmail.com"
mail_user="caivenus2019@gmail.com"
mail_pass="Venus2003"
port=465

sender = "caivenus2019@gmail.com"
receiver="guimaihong@gmail.com"

message=MIMEText("Python mail test，Hello dear你好吗",'plain','utf-8')
subject="mail test"
message['subject']=Header(subject,'utf-8')

try:
  smtpobj = smtplib.SMTP_SSL(mail_host,port)
  smtpobj.login(mail_user,mail_pass)
  smtpobj.sendmail(sender,receiver,message.as_string())
except smtplib.SMTPException:
  print("fail to send mail")