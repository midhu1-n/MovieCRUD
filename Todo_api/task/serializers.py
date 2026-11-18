from rest_framework import serializers
from task.models import task


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=task
        fields='__all__'
        read_only_fields=['user','created']
