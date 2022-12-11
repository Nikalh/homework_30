from django.urls import path

from ads.views import AdListCreateView, AdDetailView

urlpatterns = [
    path('', AdListCreateView.as_view()),
    path('<int:pk>', AdDetailView.as_view()),
]
