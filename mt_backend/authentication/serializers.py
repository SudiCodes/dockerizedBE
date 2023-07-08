from djoser.serializers import UserCreateSerializer
from authentication.models import Customer


class CustomerSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Customer
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
