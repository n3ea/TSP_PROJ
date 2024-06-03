
#tbase/tbase/main_zori/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('book', views.booking, name='book_home'),
    path('lk', views.lk, name='lk_home')

]