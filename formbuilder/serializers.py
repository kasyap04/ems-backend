from rest_framework import serializers
from formbuilder.models import DynamicForm, FormField, EmployeeRecord

class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = ['id', 'label', 'type', 'order']

class DynamicFormSerializer(serializers.ModelSerializer):
    fields = FormFieldSerializer(many=True)

    class Meta:
        model = DynamicForm
        fields = ['id', 'title', 'fields']

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        form = DynamicForm.objects.create(**validated_data)
        for field in fields_data:
            FormField.objects.create(form=form, **field)
        return form

class EmployeeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRecord
        fields = ['id', 'form', 'data', 'created_at']