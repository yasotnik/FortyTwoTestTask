from django.conf.urls import url
from apps.hello import views

app_name = 'hello'

urlpatterns = (

    # URL for index page with bio
    url(r'^$', views.ShowBioView.as_view(), name='index_bio'),

)
