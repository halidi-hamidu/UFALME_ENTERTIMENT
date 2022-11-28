from email import message
from http.client import HTTPResponse
from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
import datetime
from .forms import CustomerInformationsForm
# Create your views here.

# homepage
def homePage(request):
  template_name = 'normalUserFrontEnd/homePage.html'
  context ={}
  return render(request, template_name, context)

# aboutUs
def aboutUs(request):
  template_name = 'normalUserFrontEnd/aboutUs.html'
  context ={}
  return render(request, template_name, context)


# entertainmentsPlan
def entertainmentsPlan(request):
  template_name = 'normalUserFrontEnd/entertainmentsPlan.html'
  context ={}
  return render(request, template_name, context)

# youtubePackage
def youtubePackage(request):
  template_name="normalUserFrontEnd/subScriberPlan.html"
  context = {}
  return render(request, template_name, context)

# function for mesages
def emailMessages(package_name,customer, date,email ):
  send_mail(
        subject = f"{package_name}",
        message = f'hi {customer} Thank you for your order on {date}. We look forward to doing business with you again! ',
        from_email = 'ufalmeentertainments@gmail.com',
        recipient_list = [email,],
        auth_user = 'ufalmeentertainments@gmail.com',
        auth_password = 'bwuwubsyroacdpzz',
        fail_silently = True,
    )

# youtubeBasicPackage
def youTubeBasicPackage(request):
  if request.method =="POST":
    form = CustomerInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      email = request.POST.get('email')
      package_name = request.POST.get('package_name')
      customer = request.POST.get('first_name')
      date = datetime.datetime.now()
      messages.success(request, "Infomation sent successfull, Thank you")
      emailMessages(package_name,customer, date,email )
      return redirect('subscriber:youTubeBasicPackage') 
    else:
      messages.info(request, "Information you provide is incorrect, please try again.")
      return redirect('subscriber:youTubeBasicPackage')
  else:
    template_name = 'normalUserFrontEnd/youTubeBasicPackage.html'
    context ={}
    return render(request, template_name, context)

# youTubeStandardPackage
def youTubeStandardPackage(request):
  if request.method =="POST":
    form = CustomerInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      email = request.POST.get('email')
      package_name = request.POST.get('package_name')
      customer = request.POST.get('first_name')
      date = datetime.datetime.now()
      messages.success(request, "Infomation sent successfull, Thank you")
      emailMessages(package_name,customer, date,email )
      messages.success(request, "Infomation sent successfull, Thank you")
      return redirect('subscriber:youTubeStandardPackage')
    else:
      messages.info(request, "Information you provide is incorrect, please try again.")
      return redirect('subscriber:youTubeStandardPackage')
  else:
    template_name= 'normalUserFrontEnd/youTubeStandardPackage.html'
    context ={}
    return render(request, template_name, context)

# youTubePremiumPackage
def youTubePremiumPackage(request):
  if request.method =="POST":
    form = CustomerInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      email = request.POST.get('email')
      package_name = request.POST.get('package_name')
      customer = request.POST.get('first_name')
      date = datetime.datetime.now()
      messages.success(request, "Infomation sent successfull, Thank you")
      emailMessages(package_name,customer, date,email )
      messages.success(request, "Information sent successfull")
      return redirect("subscriber:youTubePremiumPackage")
    else:
      messages.info(request, "Information you provide is incorrect, please try again.")
      return redirect("subscriber:youTubePremiumPackage")
  else:
      template_name ='normalUserFrontEnd/youTubePremiumPackage.html' 
      context = {}
      return render(request, template_name, context)


# instagramPackage
def instagramPackage(request):
  template_name= "normalUserFrontEnd/instagramPackage.html"
  context  ={}
  return render(request, template_name, context)

  # instagramBasicPackage
def instagramBasicPackage(request):
  if request.method =="POST":
    form = CustomerInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      email = request.POST.get('email')
      package_name = request.POST.get('package_name')
      customer = request.POST.get('first_name')
      date = datetime.datetime.now()
      messages.success(request, "Infomation sent successfull, Thank you")
      emailMessages(package_name,customer, date,email )
      messages.success(request, "Information sent successfull")
      return redirect("subscriber:instagramBasicPackage")
    else:
      messages.info(request, "Information you provide is incorrect, please try again.")
      return redirect("subscriber:instagramBasicPackage")
  else:
    template_name = 'normalUserFrontEnd/instagramBasicPackage.html'
    context = {}
    return render(request, template_name, context)

# instagramStandardPackage
def instagramStandardPackage(request):
  if request.method =="POST":
    form = CustomerInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      email = request.POST.get('email')
      package_name = request.POST.get('package_name')
      customer = request.POST.get('first_name')
      date = datetime.datetime.now()
      messages.success(request, "Infomation sent successfull, Thank you")
      emailMessages(package_name,customer, date,email )
      messages.success(request, "Information sent successfull")
      return redirect("subscriber:instagramStandardPackage")
    else:
      messages.info(request, "Information you provide is incorrect, please try again.")
      return redirect("subscriber:instagramStandardPackage")
  else:
    template_name= "normalUserFrontEnd/instagramStandardPackage.html"
    context = {}
    return render(request, template_name, context) 

# instagramPremiumPackage
def instagramPremiumPackage(request):
  if request.method =="POST":
    form = CustomerInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      email = request.POST.get('email')
      package_name = request.POST.get('package_name')
      customer = request.POST.get('first_name')
      date = datetime.datetime.now()
      messages.success(request, "Infomation sent successfull, Thank you")
      emailMessages(package_name,customer, date,email )
      messages.success(request, "Information sent successfull")
      return redirect("subscriber:instagramStandardPackage")
    else:
      messages.info(request, "Information you provide is incorrect, please try again.")
      return redirect("subscriber:instagramStandardPackage")
  else:
    template_name = 'normalUserFrontEnd/instagramPremiumPackage.html'
    context = {}
    return render(request, template_name, context)

# digitalMarketingDistribution
def digitalMarketingDistribution(request):
  template_name = 'normalUserFrontEnd/digitalMarketingDistribution.html'
  context = {}
  return render (request, template_name, context)

# digitalMarketingDistributionBasicPackage
def digitalMarketingDistributionBasicPackage(request):
  if request.method =="POST":
    form = CustomerInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      email = request.POST.get('email')
      package_name = request.POST.get('package_name')
      customer = request.POST.get('first_name')
      date = datetime.datetime.now()
      messages.success(request, "Infomation sent successfull, Thank you")
      emailMessages(package_name,customer, date,email )
      messages.success(request, "Information sent successfull")
      return redirect("subscriber:digitalMarketingDistributionBasicPackage")
    else:
      messages.info(request, "Information you provide is incorrect, please try again.")
      return redirect("subscriber:digitalMarketingDistributionBasicPackage")
  else:
    template_name = 'normalUserFrontEnd/digitalMarketingDistributionBasicPackage.html'
    context = {}
    return render (request, template_name, context)


# digitalMarketingDistributionStandardPackage
def digitalMarketingDistributionStandardPackage(request):
  if request.method =="POST":
    form = CustomerInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      email = request.POST.get('email')
      package_name = request.POST.get('package_name')
      customer = request.POST.get('first_name')
      date = datetime.datetime.now()
      messages.success(request, "Infomation sent successfull, Thank you")
      emailMessages(package_name,customer, date,email )
      messages.success(request, "Information sent successfull")
      return redirect("subscriber:digitalMarketingDistributionStandardPackage")
    else:
      messages.info(request, "Information you provide is incorrect, please try again.")
      return redirect("subscriber:digitalMarketingDistributionStandardPackage")
  else:
    template_name = 'normalUserFrontEnd/digitalMarketingDistributionStandardPackage.html'
    context = {}
    return render (request, template_name, context)


# digitalMarketingDistributionPremiumPackage
def digitalMarketingDistributionPremiumPackage(request):
  if request.method =="POST":
    form = CustomerInformationsForm(request.POST)
    if form.is_valid():
      form.save()
      email = request.POST.get('email')
      package_name = request.POST.get('package_name')
      customer = request.POST.get('first_name')
      date = datetime.datetime.now()
      messages.success(request, "Infomation sent successfull, Thank you")
      emailMessages(package_name,customer, date,email )
      messages.success(request, "Information sent successfull")
      return redirect("subscriber:digitalMarketingDistributionPremiumPackage")
    else:
      messages.info(request, "Information you provide is incorrect, please try again.")
      return redirect("subscriber:digitalMarketingDistributionPremiumPackage")
  else:
    template_name = 'normalUserFrontEnd/digitalMarketingDistributionPremiumPackage.html'
    context = {}
    return render (request, template_name, context)

# earningMoneyOnline
def earningMoneyOnline(request):
  template_name = 'normalUserFrontEnd/earningMoneyOnline.html'
  context = {}
  return render (request, template_name, context)


# advertiseBussiness
def advertiseBussiness(request):
  template_name = 'normalUserFrontEnd/advertiseBussiness.html'
  context = {}
  return render (request, template_name, context)