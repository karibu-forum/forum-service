from forum_service.app.celery import celery   # noqa, this module needs "app"
from forum_service.app.initialization import initialize

initialize()
