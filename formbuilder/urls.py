from django.urls import path
from formbuilder.views import (
    CreateFormView, ListFormsView,
    SubmitEmployeeRecordView, ListEmployeeRecordsView, DeleteEmployeeRecordView
)

urlpatterns = [
    path('forms/', CreateFormView.as_view(), name='create-form'),
    path('forms/all/', ListFormsView.as_view(), name='list-forms'),
    path('records/', SubmitEmployeeRecordView.as_view(), name='submit-record'),
    path('records/<int:form_id>/', ListEmployeeRecordsView.as_view(), name='list-records'),
    path('records/delete/<int:pk>/', DeleteEmployeeRecordView.as_view(), name='delete-record'), 
]