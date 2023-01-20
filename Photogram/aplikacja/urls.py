from django.urls import path
from . import views

urlpatterns = [
    path('', views.photogram, name='photogram'),
    path('mainpage/', views.mainpage, name='mainpage-photogram'),
    path('login/', views.login, name='log-in'),
    path('signup/', views.signup, name='sign-up'),
    path('profile/', views.profile, name='profile')
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns += staticfiles_urlpatterns()