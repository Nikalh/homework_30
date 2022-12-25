from rest_framework import serializers


from users.models import User, Location


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Location.objects.all())

    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Location.objects.all())
    total_ads = serializers.SerializerMethodField()

    def get_total_ads(self, user):
        return user.ad_set.filter(is_published=True).count()

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False, many=True, slug_field='name',
                                             queryset=Location.objects.all())
    id = serializers.IntegerField(required=False)

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        pas = validated_data.pop("password")
        new_user = User.objects.create(**validated_data)
        new_user.set_password(pas)
        new_user.save()
        for loc in self._locations:
            location, created = Location.objects.get_or_create(name=loc)
            new_user.locations.add(location)

        return new_user

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Location.objects.all())
    id = serializers.IntegerField(required=False)

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)
        for loc in self._locations:
            location, created = Location.objects.get_or_create(name=loc)
            user.locations.add(location)
        return user

    class Meta:
        model = User
        exclude = ['password']


class LocationModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Location
        fields = '__all__'
