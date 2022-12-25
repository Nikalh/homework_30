from django.urls import path
from rest_framework import routers

from ads.views import *

urlpatterns = [
    # path('', AdListView.as_view()),
    # path('<int:pk>', AdDetailView.as_view()),
    # path('create/', AdCreateView.as_view()),
    # path('<int:pk>/update/', AdUpdateView.as_view()),
    # path('<int:pk>/delete/', AdDeleteView.as_view()),
    path('<int:pk>/upload_image/', AdUploadImage.as_view()),
]

router = routers.SimpleRouter()
router.register('', AdViewSet)
urlpatterns += router.urls
