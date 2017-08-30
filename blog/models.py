from django.db import models

# Create your models here.

#====================================================================================
class Article(models.Model):

	""" Model to create a blog article """

	titre = models.CharField(max_length=100)
	slug = models.SlugField()
	auteur = models.CharField(max_length=42)
	contenu = models.TextField(null=True)
	date = models.DateTimeField(verbose_name="Date de parution", auto_now_add=True, auto_now=False)
	is_visible = models.BooleanField(verbose_name="Article publié ?", default=False)
	categorie = models.ForeignKey('Categorie', verbose_name="Catégorie", related_name="categories")

	def __str__(self):

		return self.titre

    # En cas de besoin, vous êtes autorisé à rajouter des méthodes ou
    # propriétés dans ce modèle.



#====================================================================================
class Categorie(models.Model):

	""" Model to create a category of articles """

	titre = models.CharField(max_length=100)

	def __str__(self):

		return self.titre



#====================================================================================
class Comment(models.Model):

    """ Model to create comments for articles """

    article = models.ForeignKey('Article', verbose_name="Article", related_name="commentaires")
    pseudo = models.CharField("Pseudo", max_length=25)
    email = models.EmailField("Email")
    contenu = models.TextField("Contenu")
    is_visible = models.BooleanField("Commentaire visible ?", default=True)
    date = models.DateTimeField("Date de soumission", auto_now_add=True, auto_now=False)

    class Meta:
    	verbose_name = 'Commentaire'
    	verbose_name_plural = 'Commentaires'

    def __str__(self):

    	return "Commentaire [{}] posté par {} sur l'article {}".format(self.id, self.pseudo, self.article)
