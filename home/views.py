from django.views.generic import TemplateView


class Index(TemplateView):
    """
    Renders Homepage
    """
    template_name = 'home/index.html'
