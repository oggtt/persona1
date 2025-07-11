from django import forms

class QuestionForm(forms.Form):
    name = forms.CharField(label='Your name')
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')],
        label='Your gender'
    )
    radio = forms.ChoiceField(
        choices=[
            ('question1', 'Are you angry in the case you lose the credit card?'),
            ('question2', 'Do you like your parents?'),
            ('question3', 'Do you like banana?')
        ],
        label='Judgement',
        widget=forms.RadioSelect
    )