"""PROJECT BY- CODE WITH DHRUV"""
import smtplib

email = 'your@email.com'
password = '########'


def send_email(to, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, password)
    s, send_email(email, to, message)
    s.quit()


send_email('sendto@email.com', 'MESSAGE HERE')
