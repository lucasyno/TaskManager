from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView

from .forms import ProfileCreationForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({'login_form': AuthenticationForm})
        return self.render_to_response(ctx)


class RegisterView(TemplateView):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({'reg_form': ProfileCreationForm})
        return self.render_to_response(ctx)

