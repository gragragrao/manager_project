from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.views import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout

from manager.models import *


class CustomLoginView(TemplateView):
    template_name = "login.html"

    def get(self, _, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'login.html'}
            return login(self.request, *args, **kwargs)

    def post(self, _, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'login.html'}
            return login(self.request, *args, **kwargs)

    def get_next_redirect_url(self):
        redirect_url = self.request.GET.get('next')
        if not redirect_url or redirect_url == '/':
            redirect_url = '/worker_list/'
        return redirect_url


def person_registration(request, *args, **kwargs):

    if request.POST:
        form_data = request.POST

        sex = Person.MAN if form_data['sex'] == 'male' else Person.WOMAN

        person = Person(
            name=form_data['name'],
            birthday=form_data['birthday'],
            sex=sex,
            email=form_data['email'],
            address_from=form_data['address_from'],
            current_address=form_data['current_address']
        )

        person.set_password(form_data['password'])
        person.save()

        return render(request, "registration_done.html", {"email": form_data['email']})


class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        workers = Worker.objects.all().select_related('person')
        context['workers'] = workers

        return render(self.request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/login/')
