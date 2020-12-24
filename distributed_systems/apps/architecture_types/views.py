from django.http import HttpResponse
from django.template import loader

from distributed_systems.apps.architecture_types.models import ArchitectureType
from distributed_systems.apps.architectures.models import Architecture


def index(request):
    architecture_types = ArchitectureType.objects.filter(parent_type__isnull=True)
    template = loader.get_template('architecture_types/index.html')
    context = {
        'architecture_types': architecture_types
    }
    return HttpResponse(template.render(context))


def detail(request, architecture_type_id):
    sub_types = ArchitectureType.objects.filter(parent_type=architecture_type_id)
    architectures = Architecture.objects.filter(architecture_type=architecture_type_id)
    parent_type = ArchitectureType.objects.get(id=architecture_type_id)
    template = loader.get_template('architecture_types/index.html')
    context = {
        'architecture_types': sub_types,
        'architectures': architectures,
        'parent_type': parent_type,
    }
    return HttpResponse(template.render(context))
