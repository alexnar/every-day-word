from django import forms

from dict.models import NewWord


class NewWordForm(forms.ModelForm):
    word = forms.CharField(label="Ваше новое слово:", required=True)
    definition = forms.CharField(label="Ваше определение слова:", required=True, widget=forms.Textarea)

    class Meta:
        model = NewWord
        fields = ['word', 'definition', ]

    def __init__(self, *args, **kwargs):
        super(NewWordForm, self).__init__(*args, **kwargs)
