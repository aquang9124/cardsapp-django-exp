from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Card, Note
# Create your views here.
def index(request):
	cards = Card.objects.all()
	context = {
		'cards': cards,
	}
	return render(request, 'cardsapp/index.html', context)

def create_card(request):
	if len(request.POST['title']) < 8:
		messages.error(request, 'Title field is required and must exceed 7 characters in length!')
		return redirect('/')
	title = request.POST['title']
	card = Card.objects.create(title=title, created_at=timezone.now(), updated_at = timezone.now())
	return redirect('/')

def show(request, card_id):
	card = Card.objects.get(id = card_id)
	notes = Note.objects.filter(card = card)
	context = {
		'card': card,
		'notes': notes,
	}

	return render(request, 'cardsapp/show.html', context)

def create_note(request, card_id):
	if len(request.POST['body']) < 10:
		messages.error(request, 'Your note cannot be less than 10 characters in length.')
		return redirect('/card/%s' % str(card_id))
	body = request.POST['body']
	card = Card.objects.get(id = card_id)
	Note.objects.create(body=body, card = card, created_at = timezone.now(), updated_at=timezone.now())
	
	return redirect('/card/%s' % str(card_id))