from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/$',views.profile,name = 'NewProfile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit_profile/$',views.edit_profile,name = 'edit_profile'),
    url(r'^businesses/$',views.businesses,name = 'businesses'),
    url(r'^new_business/$',views.new_business,name = 'new_business'),
    url(r'^search/', views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)