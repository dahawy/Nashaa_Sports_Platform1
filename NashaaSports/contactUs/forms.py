from django import forms
from .models import CustomerQuery

class CustomerQueryForm(forms.ModelForm):
    class Meta:
        model = CustomerQuery
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input block w-full px-4 py-3 mb-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'الاسم'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input block w-full px-4 py-3 mb-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'الايميل'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input block w-full px-4 py-3 mb-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'العنوان'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea block w-full px-4 py-3 mb-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'rows': 5,
                'placeholder': 'رسالتك...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select block w-full px-4 py-3 mb-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
        }