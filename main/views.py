from django.shortcuts import render
from main.models import Domain, RecordType, ChangePoint
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def table(request):
    now = datetime.now()
    a_day_ago = now - timedelta(days=1)
    domains = Domain.objects.filter(enabled=True)
    record_types = RecordType.objects.filter(enabled=True)
    change_point_countss = dict([domain.name, dict([record_type.name, 0] for record_type in record_types)] for domain in domains)
    change_point_lastss = dict([domain.name, dict([record_type.name, None] for record_type in record_types)] for domain in domains)
    for domain in domains:
        for record_type in record_types:
            change_point_countss[domain.name][record_type.name] = ChangePoint.objects.filter(domain=domain, record_type=record_type, time__range=[a_day_ago, now]).count()
            if change_point_countss[domain.name][record_type.name] >= 0:
                change_point_lastss[domain.name][record_type.name] = ChangePoint.objects.filter(domain=domain, record_type=record_type).last().value
    context = {
        'domains': [ domain for domain in domains ],
        'record_types': [ record_type for record_type in record_types ],
        'change_point_countss': change_point_countss,
        'change_point_lastss': change_point_lastss
    }
    return render(request, 'table.html', context)

def list(request):
    context = {}
    return render(request, 'home.html', context)

def item(request, domain_id, record_type_id):
    change_points = ChangePoint.objects.filter(domain=domain_id, record_type=record_type_id).order_by('-time')[:64]
    context = {'change_points': change_points}
    return render(request, 'item.html', context)

