import yagmail

user = 'jsankalp30@gmail.com'
app_password = 'gmailTokenPassword' # a token for gmail
to = 'sankalp.jain3998@gmail.com'

subject = 'test subject 1'
content = ['mail body content','pytest.ini','test.png']

with yagmail.SMTP(user, app_password) as yag:
    yag.send(to, subject, content)
    print('Sent email successfully')