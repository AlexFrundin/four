from rest_framework import serializers
from .models import TestModel

class TestModelSerializeAll(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('id','name')

class TestModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields =  '__all__'

    # image = serializers.SerializerMethodField()
    #
    # def get_image(self, model):
    #     request = self.context.get('request')
    #     image_url = model.foto.url
    #     return request.build_absolute_uri(image_url)
