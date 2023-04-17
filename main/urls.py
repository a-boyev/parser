from django.urls import path
from main.views import ParserView

urlpatterns = [
    path("", ParserView.as_view())
]
