import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결 확인
    smtp.starttls() # 암호화 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    subject = "test mail" # 메일 제목
    body = "mail body" # 메일 본문
    
    msg = f"Subject: {subject}\n{body}"
    
    # 발신자, 수신자, 정해진 형식의 메시지
    smtp.sendmail(EMAIL_ADDRESS, "icemen919@gmail.com", msg)