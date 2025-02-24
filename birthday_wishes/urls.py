from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.game, name='game'),
    path('dialogue/<int:dialogue_id>', views.get_dialogue, name='get_dialogue'),
]