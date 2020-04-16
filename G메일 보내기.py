import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "daun3046@gmail.com" # 보내는 사람 메일 주소
my_password = "---------" # 보내는 사람 메일 비밀번호
you = "daun@gmail.com" # 받는 사람 메일 주소

msg = MIMEMultipart('alternative') # 이메일 작성 form 받아오기
msg['Subject'] = "알림" # 제목 입력
msg['From'] = me # 송신자 입력
msg['To'] = you # 수신자 입력

html = '알림 보내기 성공' # 이메일 내용 작성
part2 = MIMEText(html, 'html') # 이메일 내용의 타입
msg.attach(part2) # 이메일 form에 작성 내용 입력

s = smtplib.SMTP_SSL('smtp.gmail.com') # gmail로 전달할 것임을 표시
s.login(me, my_password) # 계정 정보로 로그인
s.sendmail(me, you, msg.as_string()) # 이메일 보내기 프로그램 종료
s.quit()