from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils.html import strip_tags
from .models import Article, Comment
from .forms import CommentForm


# Create your views here.


def accueil(request):

    """Affiche les 5 derniers articles du blog. 

    Nous n'avons pas encore vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.

    """

    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]

    return render(request, 'blog/accueil.html', {'articles': articles})


def lire_article(request, slug):

    """ Affiche un article complet, sélectionné en fonction du slug fourni en paramètre """
    
    article = get_object_or_404(Article, slug=slug)

    form = CommentForm(request.POST or None)

    if form.is_valid():

    	pseudo = form.cleaned_data['pseudo']
    	email = form.cleaned_data['email']
    	contenu = strip_tags(form.cleaned_data['contenu'])
    	Comment.objects.create(article=article, pseudo=pseudo, email=email, contenu=contenu)

    	form = CommentForm(None) # reset the fields of the form

    return render(request, 'blog/lire_article.html', locals())






