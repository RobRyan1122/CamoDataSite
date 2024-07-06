from django.urls import path
from . import views

from .views import home
from .views import image_list, nth_image, create_question, start_session  # Make sure to import first_image

urlpatterns = [
    path('', home, name='home'),
    path('images/', views.image_list, name='image_list'),
    path('nth-image/', nth_image, name='nth_image'),
    path('create-question/', create_question, name='create_question'),
    path('start-session/', start_session, name='start_session'),
    path('thanks/', views.thanks, name='thanks'),
]
