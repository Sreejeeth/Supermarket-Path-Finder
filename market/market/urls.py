"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
#from .views import home, register
from supermarket import views as core_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', core_views.front, name='home'),
    url(r'^home/$', core_views.home, name='home'),
    url(r'^admin/', admin.site.urls),   
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
   url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
     url(r'^logout/$', auth_views.LogoutView, {'next_page': 'login'}, name='logout'),
     url(r'^front2/$', core_views.front2, name='front2'),
      url(r'^virtual/$', core_views.virtual, name='virtual'),
    # url(r'^logout/$',
    # auth_views.LogoutView,
    # {'next_page': reverse_lazy("dashboard:operations_login")},
    # name="operations_logout"),
    url(r'^signup/$', core_views.signup, name='signup'),
 url(r'^home2/', core_views.help ,name='home2'),
  url(r'^home3/', core_views.home3 ,name='home3'),
      url(r'^about/', core_views.about ,name='about'),
# url(r'^about/',core_views.about, name='about'),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^product_list/$', core_views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', core_views.product_list, name='product_list_by_category'),
    # url(r'^product_list/$', core_views.product_list, name='product_list'),
    # url(r'^(?P<category_slug>[-\w]+)/$', core_views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',core_views.product_detail,name='product_detail'),

url(r'^about1/', core_views.about ,name='about1'),
   

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     url(r'^$',core_views.front, name='front'),
#     url(r'home', core_views.home, name='home'),
#     # url(r'^register/', register),
#     # url(r'^login/$', auth_views.LoginView),
#     url(r'^signup/$', core_views.signup, name='signup'),
#     #url(r'^login/$', auth_views.LoginView, {'template_name': 'login.html'})
    # url(r'^logout/$', auth_views.logout)
    #url(r'^', include('supermarket.urls'))
    # url(r'^accounts/login/$', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),
    # #url( r'^account/login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    # url(r'^logout/$', auth_views.LogoutView, {'next_page': 'login'}, name='logout'),
    # url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'^admin/', admin.site.urls),
    
