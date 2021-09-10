from django.views.generic import TemplateView


class TodoBaseTemplate(TemplateView):
    template_name = "todo/index.html"
