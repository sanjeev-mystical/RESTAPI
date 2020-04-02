from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Status
from .serializers import StatusSerializer
from accounts.api.permissions import IsOwnerOrReadOnly
import json

# # CreateModelMixin -- POST method
# # UpdateModelMixin -- PUT method
# # DestroyModelMixin -- DELETE method


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class StatusApiDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user=self.request.user)

    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None


class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    passed_id = None
    search_fields = ('user__username', 'content', 'user__email')
    ordering_fields = ('user_username', 'timestamp')
    queryset = Status.objects.all()


    # def get_queryset(self):
    #     request = self.request
    #     # print(request.user)
    #     qs = Status.objects.all()
    #     query = request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#
# # CreateModelMixin -- POST method
# # UpdateModelMixin -- PUT method
# # DestroyModelMixin -- DELETE method
#
# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('qs')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#
# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
