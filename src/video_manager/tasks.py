from celery import shared_task
import time


@shared_task
def metadata_pull():
    print('Stuff is happening...')
    time.sleep(5)  # Sleep for 5 seconds before printing again
    return 'STUFF'
