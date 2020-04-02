import json
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update
from django.views.generic import View


def update_model_detail_view(request):
    data = {
        "count": 1000,
        "content": "some new content"
    }
    return JsonResponse(data)


class HttpResponseMixin(object):
    is_json = False

    def render_to_response(self, data, status=200):
        content_type = 'text/html'
        if self.is_json:
            content_type = 'application/json'
        return HttpResponse(data, content_type=content_type, status=status)


class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context


class JsonCBV(View):

    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):

    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "some new content"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')
