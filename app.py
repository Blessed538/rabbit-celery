from flask import Flask, request
from celery_config import celery
from email_service import send_email_task
from logger import log_message

app = Flask(__name__)

@app.route('/')
def index():
    sendmail_param = request.args.get('sendmail')
    talktome_param = request.args.get('talktome')

    if sendmail_param:
        send_email_task.delay(sendmail_param)  # Queue the email sending task
        return f'Email task queued {sendmail_param}'

    if talktome_param is not None:
        log_message()
        return 'Current time logged!'

    return 'Provide ?sendmail or ?talktome parameters!'


if __name__ == '__main__':
   app.run(debug=True, port=5001) 

