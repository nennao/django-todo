from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from accounts.views import UserView

urlpatterns = [
    url(r'^register/$', UserView.as_view()),
    url(r'^api-token-auth/$', obtain_jwt_token),
    # url(r'^(?P<pk>[0-9]+)/$', UserView.as_view()),
    # url(r'^$', UserView.as_view())
]