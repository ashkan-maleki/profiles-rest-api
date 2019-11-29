from rest_framework import serializers

from profiles_api.models import UserProfile


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        # user = UserProfile(
        #     email=validated_data['email'],
        #     username=validated_data['username'],
        #     password=validated_data['password']
        # )
        print(validated_data)
        user = UserProfile(**validated_data)
        user.save()
        return user