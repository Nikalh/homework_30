from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.permissions import *
from ads.serializer import SelectionSerializer, SelectionListSerializer, SelectionDetailSerializer, \
    SelectionCreateSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    default_serializer = SelectionSerializer
    serializer_classes = {
        'list': SelectionListSerializer,
        'retrieve': SelectionDetailSerializer,
        'create': SelectionCreateSerializer
    }

    default_permission = [AllowAny()]
    permission = {
        "create": [IsAuthenticated()],
        "retrieve": [IsAuthenticated()],
        "update": [IsAuthenticated(), IsSelectionOwner()],
        "partial_update": [IsAuthenticated(), IsSelectionOwner()],
        "destroy": [IsAuthenticated(), IsSelectionOwner()]
    }

    def get_permissions(self):
        return self.permission.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)
