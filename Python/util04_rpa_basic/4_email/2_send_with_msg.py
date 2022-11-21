import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "icemen919@gmail.com" # 받는 사람

# 여러명에게 메일을 보낼때
# msg["To"] = "id1@gmail.com, id2@gmail.com"
# to_list = ["id1@gmail.com","id2@gmail.com"]
# msg["To"] = ", ".join(to_list)

# 참조
# msg["Cc"] = "id@gmail.com"

# 비밀참조
# msg["Bcc"] = "id@mail.com"

msg.set_content("테스트 본문입니다") # 본문

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo() # 연결 확인
    smtp.starttls() # 암호화 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)