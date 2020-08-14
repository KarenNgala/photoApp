from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.feed, name='feed'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^user/(\d+)/$', views.user, name='users'),
    url(r'new/image$', views.new_image, name='new_image'),
    url(r'comments/(\d+)/', views.comments, name='comments'),
    url(r'like/(\d+)/$',views.like_post, name='like' ),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)