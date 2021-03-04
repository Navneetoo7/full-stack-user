from django.db.models import fields
from rest_framework  import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'user_image', 'email', 'institution', 'loft', 'country', 'password']
    # first_name = serializers.CharField(max_length=100)
    # last_name = serializers.CharField(max_length=100)
    # email = serializers.EmailField(max_length=100)
    # institution = serializers.CharField(max_length=100)
    # loft = serializers.CharField(max_length=100)
    # country = serializers.CharField(max_length=10)

    # def create(self, validated_data):
    #     return Users.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.title= validated_data   
