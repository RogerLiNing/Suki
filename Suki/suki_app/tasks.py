from __future__ import absolute_import, unicode_literals
from celery import shared_task

import datetime

@shared_task
def print_time():
    # 输入当前时间
    print(datetime.datetime.now())
