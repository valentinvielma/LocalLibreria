from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
	#Generar contadores de algunos objetos.
	num_books= Book.objects.all().count()
	num_instances=BookInstance.objects.all().count()

	#Libros disponibles (estado='a')
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()
	num_authors=Author.objects.count() #El 'all()' esta implicito por defecto.

	#renderiza la plantilla html index.html con los datos en las variables contexto
	return render(
		request,
		'index.html',
		context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
	)
