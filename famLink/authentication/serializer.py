from rest_framework import serializers

class LoginSerializers(serializers.Serializer):
    idToken = serializers.CharField(required=True)
