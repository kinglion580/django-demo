from django import forms


class FileForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'fileupload', 'multiple': True}))
