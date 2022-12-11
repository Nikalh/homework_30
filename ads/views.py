import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def root(request):
    return JsonResponse({"status": "Ok"})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({"id": category.pk, "name": category.name})


class AdDetailView(DetailView):
    model = Ad
    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({"id": ad.pk,
                             "name": ad.name,
                             "author": ad.author,
                             "price": ad.price,
                             "description": ad.description,
                             "address": ad.address,
                             "is_published": ad.is_published,
                             })


@method_decorator(csrf_exempt, name='dispatch')
class AdListCreateView(View):
    def get(self, request):
        ad_list = Ad.objects.all()
        return JsonResponse([{"id": ad.pk,
                              "name": ad.name,
                              "author": ad.author,
                              "price": ad.price,
                              "description": ad.description,
                              "address": ad.address,
                              "is_published": ad.is_published, } for ad in ad_list], safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)
        new_ad = Ad.objects.create(**ad_data)
        return JsonResponse({"id": new_ad.pk,
                             "name": new_ad.name,
                             "author": new_ad.author,
                             "price": new_ad.price,
                             "description": new_ad.description,
                             "address": new_ad.address,
                             "is_published": new_ad.is_published, })


@method_decorator(csrf_exempt, name='dispatch')
class CatListCreateView(View):
    def get(self, request):
        cat_list = Category.objects.all()
        return JsonResponse([{"id": cat.pk,
                              "name": cat.name,
                              } for cat in cat_list], safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        new_cat = Category.objects.create(**cat_data)
        return JsonResponse({"id": new_cat.pk,
                             "name": new_cat.name,
                             })
