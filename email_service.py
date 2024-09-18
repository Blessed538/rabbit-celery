from flask import Flask
from flask_mail import Mail, Message
from celery_config import celery

app = Flask(__name__)

# Flask-Mail configuration (use your actual email and password)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'blesseddominic98@gmail.com'
app.config['MAIL_PASSWORD'] = 'Makarios25#'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Celery task to send email asynchronously
@celery.task
def send_email_task(recipient):
    try:
        msg = Message('Hello from Flask', sender='your_email@gmail.com', recipients=[recipient])
        msg.body = "This is a test email sent using Flask and Celery."
        with app.app_context():
            mail.send(msg)
        return f'Email sent to {recipient}'
    except Exception as e:
        return str(e)
