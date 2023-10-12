from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_flex_fields import FlexFieldsModelSerializer
from microblog.serializers import *


class UserSerializer(FlexFieldsModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'posts', 'comments', 'tags')

        expandable_fields = {
            'posts': (PostSerializer, {'many': True}),
            'comments': (CommentSerializer, {'many': True}),
            'tags': (TagSerializer, {'many': True})
        }

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    
    def create(self, validated_data):
        # save user
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            message = 'Invalid credentials, please try again.'
            raise serializers.ValidationError(message, code='authentication')

        attrs['user'] = user
        return attrs   
    
class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password')

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You don\'nt have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    
class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

        def validate_email(self, value):
            user = self.content['request'].user
            if User.objects.exclude(pk=user.pk).filter(email=value).exists():
                raise serializers.ValidationError({"email": "This email is already in use."})
            return value
        
        def validate_username(self, value):
            user = self.content['request'].user
            if User.objects.exclude(pk=user.pk).filter(username=value).exists():
                raise serializers.ValidationError({"email": "This username is already in use."})
            return value
        
        def update(self, instance, validated_data):
            user = self.context['request'].user

            if user.pk != instance.pk:
                raise serializers.ValidationError({"authorize": "You don\'nt have permission for this user."})

            instance.first_name = validated_data['first_name']
            instance.last_name = validated_data['last_name']
            instance.email = validated_data['email']
            instance.username = validated_data['username']

            instance.save()

            return instance