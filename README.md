# crepes
Django course on https://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django : (Partie 2 Activité)

Pendant les deux premières parties de ce cours, nous avons utilisé comme exemple un blog, contenant une liste d’articles et quelques catégories.

Dans cet exercice, vous allez devoir rajouter un système de commentaires au blog que nous allons vous fournir. Ce système de commentaires aura les particularités suivantes : 

    N’importe qui est autorisé à poster un commentaire, aucune inscription n’est nécessaire.
    La personne devra simplement renseigner un pseudo et un e-mail valide (ce dernier sera privé et non visible par les autres utilisateurs).
    Les commentaires pourront être modérés par l’administration Django : il doit être possible de spécifier un attribut qui dit si oui ou non un commentaire est visible (par défaut, un commentaire sera visible dès sa soumission). L’utilisation de django.contrib.comments, qui est un module déprécié et sera bientôt retiré de Django, est bien entendu interdite.
    Les articles peuvent contenir du HTML mais pas les commentaires des membres.

 Pour vous donner une idée du résultat attendu, voici un aperçu du système de commentaires du corrigé-type : 
 
 http://sdz-upload.s3.amazonaws.com/prod/upload/blog-vue-article.png
 
 http://sdz-upload.s3.amazonaws.com/prod/upload/blog-admin-comments.png
 
 Ça vous inspire ? Alors lancez-vous !

Commencez par télécharger le projet de blog, qui contient déjà la gestion des articles et les templates nécessaires.

Ensuite, dans le dossier "blog" de ce projet, remplissez tout ce qui concerne les commentaires : modèle, formulaire, la/les vue(s) pour poster un commentaire et l'administration, sans oublier le nombre de commentaires de chaque article sur l'accueil. 

Enfin, envoyez le projet complet que vous compresserez dans un fichier .zip. Pensez à supprimer la base de données SQLite et les fichiers .pyc (cache de Python) potentiels. Pour que vous receviez tous les points, il faut que votre correcteur arrive à accéder à votre blog en faisant les opérations suivantes :

    1-Dézipper le projet Django que vous aurez fourni
    2-À la racine du projet, effectuer les commandes suivantes en console :

python manage.py makemigrations blog
python manage.py migrate blog
python manage.py runserver

Et ce, sans erreurs ! À vous de décider des URL pour les nouvelles pages potentielles.

Bon courage ! 
