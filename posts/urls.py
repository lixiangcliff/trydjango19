from django.conf.urls import url
from posts.views import post_home


urlpatterns = [
    url(r'^$', post_home),
]