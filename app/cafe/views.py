from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins

from core.models import Tag, Cafe

from . import serializers


class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """Return tags for the current authenticated user only"""
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(cafe__isnull=False)

        return queryset.filter(
            user=self.request.user
        ).order_by('-name').distinct()

    def perform_create(self, serializer):
        """Create a new tag"""
        serializer.save(user=self.request.user)


class CafeViewSet(viewsets.ModelViewSet):
    """Manage cafe in the datebase"""
    serializer_class = serializers.CafeSerializer
    queryset = Cafe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the cafes for the authenticated user"""
        tags = self.request.query_params.get('tags')
        queryset = self.queryset
        if tags:
            tag_ids = self._params_to_ints(tags)
            queryset = queryset.filter(tags__id__in=tag_ids)

        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Return appropritate serializer class"""
        if self.action == 'retrieve':
            return serializers.CafeDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new cafe"""
        serializer.save(user=self.request.user)
