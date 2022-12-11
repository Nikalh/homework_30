from django.urls import path

from ads.views import CatListCreateView, CategoryDetailView

urlpatterns = [
    path('', CatListCreateView.as_view()),
    path('<int:pk>', CategoryDetailView.as_view()),
]
