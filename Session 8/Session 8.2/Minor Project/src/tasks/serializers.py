from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        if data['due_date'] is None:
            raise serializers.ValidationError("Due date is required.")
        return data
