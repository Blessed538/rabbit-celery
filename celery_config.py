from celery import Celery
from flask import Flask

def make_celery(app: Flask) -> Celery:
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    return celery

app = Flask(__name__)

# Configure Celery to use RabbitMQ as the broker
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = make_celery(app)
