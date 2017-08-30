from django import forms


class CommentForm(forms.Form):

	""" Form to add comment to an article """

	pseudo = forms.CharField(label="Pseudo", max_length=25)
	email = forms.EmailField(label="Email")
	contenu = forms.CharField(label="Contenu", widget=forms.Textarea)
