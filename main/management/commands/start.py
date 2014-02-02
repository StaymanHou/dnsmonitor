from django.core.management.base import BaseCommand, CommandError
from main.models import Setting, RecordType, Domain, ChangePoint
from time import sleep

class Command(BaseCommand):
    args = '<N/A>'
    help = 'Start monitor.'

    def handle(self, *args, **options):
        try:
            self.setting = Setting.objects.get(name='default')
        except Setting.DoesNotExist:
            raise CommandError('Setting does not exist')
        self.stdout.write('Monitor started')
        while 1:
            try:
                self.setting = Setting.objects.get(name='default')
            except Setting.DoesNotExist:
                raise CommandError('Setting does not exist')
            print 'haha'
            sleep(self.setting.interval)

