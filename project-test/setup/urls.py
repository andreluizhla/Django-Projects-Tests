from django.contrib import admin
from django.urls import path

from teste.views import TesteListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TesteListView.as_view()),
]
