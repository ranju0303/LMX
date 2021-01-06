# Core Django imports.
from django.views.generic import ListView, DetailView, CreateView

# Blog application imports.
from lms.models.assignment_model import Assignment
from django import forms
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'


class AssignmentListView(ListView):
    model = Assignment
    context_object_name = "assignments"
    template_name = "lms/assignment/list_assignment.html"


class AssignmentDetailView(DetailView):
    model = Assignment
    context_object_name = "assignment"
    template_name = "lms/assignment/show_assignment.html"


class CreateForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        widgets = {
            'due_date': DateInput(),
            'available_from': DateInput(),
            'until': DateInput(),
        }


class AssignmentCreateView(CreateView, ModelForm):
    model = Assignment
    context_object_name = "assignment"
    template_name = "lms/assignment/create_assignment.html"
    form_class = CreateForm
