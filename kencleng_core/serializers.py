from rest_framework import serializers
from . import models


class TransaksiSerializer(serializers.ModelSerializer):
     class Meta:
         model = models.Transksi
         fields = '__all__'
         read_only_fields=('a', 'b', 'c')