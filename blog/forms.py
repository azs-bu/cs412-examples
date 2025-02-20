# blog/forms.py
# define the forms that we use for create/update/delete operations

from django import forms
from .models import Article, Comment

class CreateArticleForm(forms.ModelForm):
    '''A form to add an Article to the database.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model = Article
        # fields = ['author', 'title', 'text', 'image_url']
        fields = ['author', 'title', 'text', 'image_file']

class CreateCommentForm(forms.ModelForm):
    '''A form to add a Comment about an Article.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model = Comment
        # fields = ['article', 'author', 'text']
        fields = ['author', 'text'] # we don't want the drop-down list
