from imap_tools import MailBox
from account import *

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS,EMAIL_PASSWORD,initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=10, reverse=True):
    #     print(f"[{msg.from_}] {msg.subject}")
    # 전체 메일 가져오기
        
    # for msg in mailbox.fetch('(UNSEEN)',limit=5, reverse=True):
    #     print(f"[{msg.from_}] {msg.subject}")
    # 읽지 않은 메일 가져오기

    # for msg in mailbox.fetch('(FROM icemen919@gmail.com)',limit=5, reverse=True):
    #     print(f"[{msg.from_}] {msg.subject}")
    # 특정인으로부터 온 메일 가져오기
    
    # for msg in mailbox.fetch('(TEXT "test")',limit=5, reverse=True):
    #     print(f"[{msg.from_}] {msg.subject}")
    # 특정 글자를 포함하는 메일(본문 포함) 가져오기
    
    # for msg in mailbox.fetch('(SUBJECT "test")',limit=5, reverse=True):
    #     print(f"[{msg.from_}] {msg.subject}")
    # 특정 글자를 포함하는 메일(제목만) 가져오기
    
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2022)', limit=5, reverse=True):
    #     print(f"[{msg.from_}] {msg.subject}")
    # 특정 날짜 이후 메일 가져오기
    
    # for msg in mailbox.fetch('(ON 07-Nov-2022)', limit=5, reverse=True):
    #     print(f"[{msg.from_}] {msg.subject}")
    # 특정 날짜에 온 메일 가져오기
    
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2022 TEXT "test")', limit=5, reverse=True):
    #     print(f"[{msg.from_}] {msg.subject}")
    # 2가지 이상 조건 모두 만족하는 메일 가져오기
    
    for msg in mailbox.fetch('(OR ON 07-Nov-2022 TEXT "test")', limit=5, reverse=True):
        print(f"[{msg.from_}] {msg.subject}")
    # 조건 하나라도 만족하는 메일 가져오기