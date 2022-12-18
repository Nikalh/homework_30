from django.urls import path

from ads.views import CatListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('', CatListView.as_view()),
    path('<int:pk>', CategoryDetailView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('<int:pk>/update/', CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', CategoryDeleteView.as_view()),
]
