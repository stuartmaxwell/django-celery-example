from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import BadHeaderError, send_mail

from celery_project.settings import DEFAULT_FROM_EMAIL

logger = get_task_logger(__name__)


@shared_task(bind=True, max_retries=3)
def send_email_task(self, to, subject, message):
    logger.info(f"from={DEFAULT_FROM_EMAIL}, {to=}, {subject=}, {message=}")
    try:
        logger.info("About to send_mail")
        send_mail(subject, message, DEFAULT_FROM_EMAIL, [to])
    except BadHeaderError:
        logger.info("BadHeaderError")
    except Exception as e:
        logger.error(e)
