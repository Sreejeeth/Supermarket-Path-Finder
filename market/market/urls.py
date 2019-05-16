
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
      url(r'^compare/$', core_views.compare, name='compare'),
      url(r'^thanks/$', core_views.thanks, name='thanks'),

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
