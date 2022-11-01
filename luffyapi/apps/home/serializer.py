from rest_framework import serializers
from . import models
class BannerModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields=['name','link','img']