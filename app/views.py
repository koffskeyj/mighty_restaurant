from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy
from app.models import Order, MenuItem, CompleteForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

class IndexView(TemplateView):
    template_name = "index.html"


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/login"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    fields = ["user_type"]
    success_url = reverse_lazy("index_view")

    def get_object(self, queryset=None):
        return self.request.user.profile


class OrderCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Order
    fields = ["name", "items", "details"]
    success_url = "/"

    def test_func(self):
        return self.request.user.profile.user_type == "Server"

    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user
        return super(OrderCreateView, self).form_valid(form)


class OrderListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        if self.request.user.profile.user_type == "Server":
            return Order.objects.filter(user=self.request.user)
        if self.request.user.profile.user_type == "Owner" or "Cook":
            return Order.objects.all()


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    fields = ["name", "items", "details"]
    success_url = reverse_lazy("order_list_view")


    def test_func(self):
        return self.request.user.profile.user_type == "Server"

    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user
        return super(OrderUpdateView, self).form_valid(form)

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "app/order_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CompleteForm
        return context


class CompleteFormView(LoginRequiredMixin, FormView):
    form_class = CompleteForm
    success_url = "/accounts/profile/order_list"


    def form_valid(self, form, **kwargs):
        order_id = self.kwargs.get('pk', None)
        complete_order = Order.objects.get(id=order_id)
        if Order.objects.get(id=order_id):
            form = CompleteForm(self.request.POST or None, instance=complete_order)
            if form.is_valid():
                complete = form.save(commit=False)
                complete.user = self.request.user
                complete.save()

        return super(CompleteFormView, self).form_valid(form)


class MenuItemCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MenuItem
    fields = ["item_name", "description", "price"]
    success_url = reverse_lazy("menu_item_create_view")

    def test_func(self):
        return self.request.user.profile.user_type == "Owner"

    def form_valid(self, form):
        menu_item = form.save(commit=False)
        menu_item.user = self.request.user
        return super(MenuItemCreateView, self).form_valid(form)


class MenuItemListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return MenuItem.objects.all()
