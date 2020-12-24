from django.http import HttpResponse
from django.template import loader

from distributed_systems.apps.architectures.models import Architecture


def index(request):
    architectures = Architecture.objects.all()
    template = loader.get_template('architectures/index.html')
    context = {
        'architectures': architectures
    }
    return HttpResponse(template.render(context))


def detail(request, architecture_id):
    architecture = Architecture.objects.get(id=architecture_id)
    template = loader.get_template('architectures/architecture.html')
    context = {
        'architecture': architecture
    }
    return HttpResponse(template.render(context))
