from django.db.models import Q
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView

from distributed_systems.apps.architectures.models import Architecture


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}))


class SearchResultsView(ListView):
    model = Architecture
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return
        return Architecture.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
