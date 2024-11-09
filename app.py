from os import getenv
from flask import Flask, request
from email.message import EmailMessage
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('GOOGLE_PSW')
gpsw = app.config['SECRET_KEY']


def send_message(desde, para, msg):

    # email instance
    email = EmailMessage()

    # email config
    email['From'] = desde
    email['To'] = para
    email['Subject'] = 'Bienvenida'

    # HTML message with inline CSS
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <h1 style="color: #007bff;">¡Bienvenido!</h1>
        <p>{msg}</p>
        <p style="font-size: 12px; color: #888;">Gracias por unirte a nuestra comunidad.</p>
    </body>
    </html>
    """
    # Set content as HTML
    email.add_alternative(html_content, subtype='html')

    smtp = smtplib.SMTP_SSL('smtp.gmail.com')
    smtp.login(desde, f'{gpsw}')
    smtp.sendmail(desde, para, email.as_string())
    smtp.quit()


@app.route('/email', methods=['POST'])
def send_mail():
    datos = request.json
    desde = 'nigelljama@gmail.com'
    para = datos['email']
    msg = datos['message']
    send_message(desde, para, msg)
    return {'message': 'sent'}


if __name__ == "__main__":
    app.run(port=5002, debug=True)
