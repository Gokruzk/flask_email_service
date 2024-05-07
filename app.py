from flask import Flask, request
from email.message import EmailMessage
import smtplib


app = Flask(__name__)


def send_message(desde, para):
    # Welcome message
    msg = f'Welcome {para}'

    # email instance
    email = EmailMessage()

    # email config
    email['From'] = desde
    email['To'] = para
    email['Subject'] = 'Welcome'
    email.set_content(msg)

    smtp = smtplib.SMTP_SSL('smtp.gmail.com')
    smtp.login(desde, 'rnkd lcbm yxbt xwnc')
    smtp.sendmail(desde, para, email.as_string())
    smtp.quit()


@app.route('/email', methods=['POST'])
def send_mail():
    # retreiving email
    datos = request.json
    desde = 'nigelljama@gmail.com'
    para = datos['email']
    # sending email
    send_message(desde, para)
    return {'message': 'sent'}


if __name__ == "__main__":
    app.run(port=5002, debug=True)
