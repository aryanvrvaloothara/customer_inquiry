import random

from django.contrib import messages
from django.shortcuts import render, redirect

from inquiry.forms import MobileVerificationForm, OtpForm, InquiryForm
from inquiry.functions import send_otp
from inquiry.models import Otp


def verify_mobile_number(request):
    form = MobileVerificationForm()
    if request.method == 'POST':
        form = MobileVerificationForm(request.POST)
        if form.is_valid():
            otb_obj = form.save()
            otb_obj.otp = random.randrange(1000, 9999)
            otb_obj.save()
            try:
                request.session['mobile_number'] = form.cleaned_data['mobile_number']
                send_otp(mobile_number=form.cleaned_data['mobile_number'], otp=otb_obj.otp)
                messages.success(request, 'Otp sent to your mobile.')
                return redirect('enter_otp')
            except:
                messages.error(request, 'Sorry, unexpected error occured from our side.')
                return redirect('verify_mobile_number')

    context = {
        'title': 'Verify',
        'form': form
    }
    return render(request, "verify_mobile_number.html", context)


def verify_otp(request):
    mobile_number = request.session['mobile_number']
    form = OtpForm()
    if request.method == 'POST':
        form = OtpForm(request.POST)
        if form.is_valid():
            otp_obj = Otp.objects.filter(mobile_number=mobile_number).last()
            if otp_obj.otp == form.cleaned_data['otp']:
                return redirect('inquiry')
            else:
                messages.error(request, 'Wrong OTP')
    context = {
        'title': 'OTP',
        'form': form
    }
    return render(request, "enter_otp.html", context)


def inquiry(request):
    mobile_number = request.session['mobile_number']
    form = InquiryForm()
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry_obj = form.save()
            inquiry_obj.mobile_number = mobile_number
            inquiry_obj.save()
            messages.success(request, 'Submitted successfully')
            return redirect('verify_mobile_number')
    context = {
        'title': 'Inquiry',
        'form': form
    }
    return render(request, "inquire.html", context)
