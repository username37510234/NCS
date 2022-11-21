from imap_tools import MailBox
from account import *

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS,EMAIL_PASSWORD,initial_folder="INBOX") as mailbox:
    for idx, msg in enumerate(mailbox.fetch(limit=5, reverse=False)):
        print(f"[{msg.from_}] {msg.subject}")
        if idx <3:
            print(f"{msg.from_}님 축하드립니다 (선정순번 {idx+1}번)")
        else:
            print(f"{msg.from_}님 아쉽게도 탈락입니다. (대기순번 {idx-2}번)")