import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "icemen919@gmail.com" # 받는 사람
msg.set_content("다운로드 하세요")

# msg.add_attachment()
with open("img.png","rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png",filename=f.name)

with open("scores.xlsx","rb") as f: # MIME 타입
    msg.add_attachment(f.read(), maintype="application", subtype="xls",filename=f.name)

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo() # 연결 확인
    smtp.starttls() # 암호화 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)