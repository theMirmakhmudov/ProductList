from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from .forms import SignupForm, LoginForm, InputContact
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from .models import Product, Home1, Home2, About1, AboutPerson, ContactForm, Contact


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)


class HomeView(ListView):
    template_name = 'home.html'
    model = Home1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home1"] = Home1.objects.all()
        context["home2"] = Home2.objects.all()
        return context


class AboutView(ListView):
    template_name = 'about.html'
    model = About1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About1.objects.all()
        context["about_person"] = AboutPerson.objects.all()
        return context


class ContactView(CreateView):
    template_name = 'contact.html'
    model = ContactForm
    success_url = "/"
    form_class = InputContact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contactform"] = ContactForm.objects.all()
        context["contact"] = Contact.objects.all()
        return context


class ProductView(ListView):
    template_name = 'product.html'
    model = Product
    context_object_name = 'products'
