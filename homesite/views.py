from django.views.generic import TemplateView


class HomesiteView(TemplateView):
    template_name = "homesite/index.html"
