from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from app.models import Order, MenuItem

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


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = ["items", "order_details"]
    success_url = "/"

    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user
        return super(OrderCreateView, self).form_valid(form)


class OrderListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderUpdateView(LoginRequiredMixin, ListView):
    model = Order
    fields = ["items", "order_details"]
    success_url = reverse_lazy("order_list_view")


class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    fields = ["item_name", "description", "price"]
    success_url = reverse_lazy("menu_item_create_view")

    def form_valid(self, form):
        menu_item = form.save(commit=False)
        menu_item.user = self.request.user
        return super(MenuItemCreateView, self).form_valid(form)


class MenuItemListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return MenuItem.objects.all()