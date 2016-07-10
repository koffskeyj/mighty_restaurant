"""order_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app.views import  IndexView, UserCreateView, ProfileUpdateView, OrderCreateView, MenuItemCreateView, OrderListView, MenuItemListView, OrderUpdateView, OrderDetailView, CompleteFormView
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.http import require_POST

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^user_create/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name="profile_update_view"),
    url(r'^accounts/profile/order_create/$', OrderCreateView.as_view(), name="order_create_view"),
    url(r'^accounts/profile/order_update/(?P<pk>\d+)/$', OrderUpdateView.as_view(), name="order_update_view"),
    url(r'^accounts/profile/order_detail/(?P<pk>\d+)/$', OrderDetailView.as_view(), name="order_detail_view"),
    url(r'^complete_form/$', require_POST(CompleteFormView.as_view()), name="complete_form_view"),
    url(r'^menu_item_create/$', MenuItemCreateView.as_view(), name="menu_item_create_view"),
    url(r'^accounts/profile/order_list/$', OrderListView.as_view(), name="order_list_view"),
    url(r'^menu_item_list/$', MenuItemListView.as_view(), name="menu_item_list_view")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
