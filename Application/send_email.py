import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate


from_address = 'from@xxx.xx.jp'
to_address = 'to@xxx.xx.jp'

# 文字コード
charset = 'ISO-2022-JP'
subject = 'メールの件名です'
text = 'メールの本文です'

msg = MIMEText(text, 'plain', charset)
msg['Subject'] = Header(subject, charset)
msg['From'] = from_address
msg['To'] = to_address
msg['Date'] = formatdate(localtime=True)

smtp = smtplib.SMTP('xxx.xx.jp')
smtp.sendmail(from_address, to_address, msg.as_string())
smtp.close()
