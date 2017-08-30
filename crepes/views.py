from django.shortcuts import render, redirect

def main_home(request):

    """ A view to redirect the user to the blog home, when he try to access the main home """

    return redirect('accueil')

