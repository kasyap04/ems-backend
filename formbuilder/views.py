from rest_framework import generics, filters
from formbuilder.models import DynamicForm, EmployeeRecord
from formbuilder.serializers import DynamicFormSerializer, EmployeeRecordSerializer


class CreateFormView(generics.CreateAPIView):
    queryset = DynamicForm.objects.all()
    serializer_class = DynamicFormSerializer


class ListFormsView(generics.ListAPIView):
    queryset = DynamicForm.objects.all()
    serializer_class = DynamicFormSerializer


class SubmitEmployeeRecordView(generics.CreateAPIView):
    queryset = EmployeeRecord.objects.all()
    serializer_class = EmployeeRecordSerializer


class ListEmployeeRecordsView(generics.ListAPIView):
    serializer_class = EmployeeRecordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['data']


    def get_queryset(self):
        form_id = self.kwargs['form_id']
        return EmployeeRecord.objects.filter(form_id=form_id)
    


class DeleteEmployeeRecordView(generics.DestroyAPIView):
    queryset = EmployeeRecord.objects.all()
    serializer_class = EmployeeRecordSerializer
    lookup_field = 'pk'