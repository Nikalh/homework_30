from rest_framework import routers

from ads.view_selections import SelectionViewSet

urlpatterns = [

]
router = routers.SimpleRouter()
router.register('', SelectionViewSet)
urlpatterns += router.urls
