from django.views import generic
from .models import Task

# Class View of index page
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_tasks'

    def get_queryset(self):
        """Return all tasks."""
        return Task.objects.all()