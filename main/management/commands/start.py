from django.core.management.base import BaseCommand, CommandError
from main.models import Setting, RecordType, Domain, ChangePoint
from time import sleep
import dns.resolver

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
            record_types = RecordType.objects.filter(enabled=True)
            domains = Domain.objects.filter(enabled=True)
            for domain in domains:
                for record_type in record_types:
                    last_change_point = ChangePoint.objects.filter(domain=domain, record_type=record_type).last()
                    new_change_point = ChangePoint()
                    try :
                        answers = dns.resolver.query(domain.name, record_type.name)
                    except Exception, e:
                        new_change_point.value = str(e.__class__)
                    else:
                        new_change_point.value = '|'.join([ str(answer) for answer in answers ].sort())
                    if last_change_point is None or new_change_point.value != last_change_point.value:
                        new_change_point.domain = domain
                        new_change_point.record_type = record_type
                        new_change_point.save()
            sleep(self.setting.interval)
