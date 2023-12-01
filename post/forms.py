from django import forms
from post.models import Equipment, Category

class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    price = forms.IntegerField(required=True)
    rate = forms.IntegerField(min_value=1, max_value=10)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Title too short!')
        return cleaned_data

    # def clean_description(self):
    #     cleaned_data = super().clean()
    #     description = cleaned_data.get('description')
    #     if len(description) < 10:
    #         raise forms.ValidationError('Description too short!')
    #     if not description:
    #         raise forms.ValidationError('Description is required!')
    #
    #     return cleaned_data


class PostCreateForm2(forms.Form):
    class Meta:
        model = Equipment
        fields = ['title', 'description', 'image', 'price', 'rate']

class CategoryCreateForm(forms.Form):
    title = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Title too short!')
        return cleaned_data


class FeedbackCreateForm(forms.Form):
    title = forms.CharField()
