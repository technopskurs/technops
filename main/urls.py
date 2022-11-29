from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.LoginUser.as_view(), name='login'),
    path("registration/", views.Register.as_view(), name="registration"),
    path('accounts/', include('django.contrib.auth.urls'))

]