import gspread
import sys
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NorthValleyContactForm
from django.conf import settings
from datetime import datetime
from django.core.mail import send_mail
from django.http import JsonResponse


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request) :
	return render(request, "landings/index.html")

def north_valley(request):
	if request.method == 'POST':
		try:
			form = NorthValleyContactForm(request.POST)
			#if form.is_valid():
			#print('form is valid')
			gc = gspread.service_account()
			wks = gc.open(settings.NORTH_VALLEY_SHEET_NAME).sheet1
			dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
			wks.append_row([
				'',
				form.data['name'],
				form.data['email'],
				form.data['phone'],
				dt,
				request.META['HTTP_USER_AGENT'],
				get_client_ip(request)])
			message = "Дата: {}\n ФИО: {}\n email:{}\n Телефон: {}".format(dt, form.data['name'], form.data['email'], form.data['phone'])
			print(message)
			#send_mail("Новая запись. Северная долина", message, "k.svyatov@ulstu.ru", ["k.svyatov@gmail.com"])
			return JsonResponse({'result': 'ok'})  # HttpResponseRedirect('/landings/northvalley/#contact')
		except Exception:
			exc_type, exc_value, exc_traceback = sys.exc_info()
			msg = "exception in form sending: ", exc_type, exc_value, exc_traceback
			print(msg)
			return JsonResponse({'result': 'error', 'data':msg})

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NorthValleyContactForm()
		print(request.META)
		return render(request, 'landings/north_valley.html', {'form': form})

def enter(request):
	return render(request, 'landings/enter.html')

def index(request):
	return render(request, 'landings/index.html')
