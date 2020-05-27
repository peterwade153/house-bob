from django.core.management import call_command

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute=0,hour=0, day_of_week=0)))
def crawl_properties():
    call_command('crawl')
    logger.info("Properties scraped")
