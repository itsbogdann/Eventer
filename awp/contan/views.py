from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from models import *
from random import randint
from django.core.mail import send_mail
from . import models
import json



def index(request):
    status_list = models.Status.objects.all()
    return render(request, 'contan/index.html',
                  {'status_list': status_list})

def register(request):

	user_email = ""
	user_password = ""
	user_name = ""
	user_school = ""

 	if request.method == 'POST':

		eemail = request.POST.get("useremail")
		pparola = request.POST.get("userpassword")
		nnume = request.POST.get("username")
		sscoala = request.POST.get("userschool")

		if (User.objects.filter(email=eemail).count()<1):
			
			utilizator = User()

			utilizator.email = eemail
			utilizator.scoala = sscoala
			utilizator.parola = pparola
			utilizator.nume = nnume

			utilizator.save()

		
		
			#send_mail(subject,message,from_email,to_email,fail_silently=True)

			return JsonResponse({"id":"1"})
		else:
			return JsonResponse({"id":"0"})
		

	else:
		return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



def login(request):
	if request.method == 'POST':
		eemail = request.POST.get("useremail")
		pparola = request.POST.get("userpassword")

		if (User.objects.filter(email=eemail, parola=pparola).count()==1):
			return JsonResponse({"idLogin":"1"})
		else:
			return JsonResponse({"idLogin":"0"})
	else:
		return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def classes(request):

	univ = College()
	#mn = College()
	mn = []
	curs = ""
	univ = ""
	lista = []

	print request.POST

	if request.method == 'POST':
		curs = request.POST.get("className")
		univ = request.POST.get("universityName")


		if curs and univ:
			mn = College.objects.get(nume=univ)
			if (curs in mn.cursuri) or (mn.cursuri in curs):
					return JsonResponse({"id":"1"})
			else:
				return JsonResponse({"id":"0"})

		if (not curs) and (not univ):
			return JsonResponse({"id":"0"})

		if curs and (not univ):
			mn = College.objects.all()
			for i in mn:
				if (i.cursuri in curs) or (curs in i.cursuri):
					lista.append(i.nume)

			d = {"Facultati":lista}
			return JsonResponse(d)


		if (not curs) and univ:
			mn = College.objects.filter(nume=univ)
			for i in mn:
				st = i.cursuri.split(',')
				d = {"Cursuri":st}
			return JsonResponse(d)
				


	else:
		return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



def personalclasses(request):
	pf = []
	d = {}
	lista = []
	if request.method == 'POST':
		#username = request.POST.get("user")
		d = json.loads(request.body)
		username = d['user']

		pf = User.objects.filter(email=username)
		print pf
		for i in pf : 
			lista = i.cursuri_inscris.split(',')
			
		d = {"id": lista}
		return JsonResponse(d)


def checks(request):
	k=0
	d = json.loads(request.body)
	mn = User()
	m = len(d['classes'])
	#User.objects.filter(nume=d['user']).update(cursuri_inscris=d['classes']+" "+d['universities'])
	mn = User.objects.filter(nume=d['user'])
	
	for i in mn:
		i.update(cursuri_inscris = d['classes'][k])
		k+=1
		i.save()
	return JsonResponse({})



def csrf_failure(request, reason=""):
	print "FAIL CSRF!!!!!"