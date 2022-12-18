
import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from users.models import User, Location


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse({"id": user.pk,
                             "first_name": user.first_name,
                             "last_name": user.last_name,
                             "username": user.username,
                             "role": user.role,
                             "locations": [loc.name for loc in user.locations.all()],
                             "age": user.age
                             })


@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListView):
    model = User
    queryset = User.objects.order_by('username')

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        users = [{"id": user.pk,
                  "first_name": user.first_name,
                  "last_name": user.last_name,
                  "username": user.username,
                  "role": user.role,
                  "locations": [loc.name for loc in user.locations.all()],
                  "age": user.age,
                  "total_ads": user.ad_set.filter(is_published=True).count()
                  } for user in self.object_list]

        return JsonResponse(users, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        new_user = User.objects.create(
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            username=user_data.get('username'),
            password=user_data.get('password'),
            role=user_data.get('role'),
            age=user_data.get('age')

        )
        for loc in user_data.get('locations'):
            location, created = Location.objects.get_or_create(name=loc)
            new_user.locations.add(location)
        return JsonResponse({"id": new_user.pk,
                             "first_name": new_user.first_name,
                             "last_name": new_user.last_name,
                             "username": new_user.username,
                             "role": new_user.role,
                             "locations": [loc.name for loc in new_user.locations.all()],
                             "age": new_user.age
                             })

@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = "__all__"

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        if 'username' in user_data:
            self.object.username = user_data['username']
        if 'first_name' in user_data:
            self.object.first_name = user_data['first_name']
        if 'last_name' in user_data:
            self.object.last_name = user_data['last_name']
        if 'age' in user_data:
            self.object.age = user_data['age']
        if 'locations' in user_data:
            for loc in user_data.get('locations'):
                location, _ = Location.objects.get_or_create(name=loc)
                self.object.locations.add(location)
        return JsonResponse({"id": self.object.pk,
                             "first_name": self.object.first_name,
                             "last_name": self.object.last_name,
                             "username": self.object.username,
                             "role": self.object.role,
                             "locations": [loc.name for loc in self.object.locations.all()],
                             "age": self.object.age
                             })




@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user_pk = user.pk
        super().delete(request, *args, **kwargs)
        return JsonResponse({"id": user_pk.pk})
