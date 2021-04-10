from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
	return render(request, 'index.html')


def meanings(request):
	search = request.GET.get('search')
	dictionary = PyDictionary()
	meaning = dictionary.meaning(search)
	context = {
		'meaning': meaning['Noun'][0]
	}

	return render(request, 'meanings.html', context)