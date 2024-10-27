from django.contrib import admin
from django.urls import path

from questions.views import GetRandomQuestion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/<int:telegram_id>', GetRandomQuestion.as_view())
]
