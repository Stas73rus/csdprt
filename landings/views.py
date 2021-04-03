import gspread
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NorthValleyContactForm
from django.conf import settings
from datetime import datetime
from django.core.mail import send_mail

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
			print(form.data['name'], form.data['email'], form.data['phone'])
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
			send_mail("Новая запись. Северная долина", message, "k.svyatov@ulstu.ru", ["k.svyatov@gmail.com"])
		except:
			print("exception in form sending")
		return HttpResponseRedirect('/landings/northvalley/#contact')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NorthValleyContactForm()

	return render(request, 'landings/north_valley.html', {'form': form})

