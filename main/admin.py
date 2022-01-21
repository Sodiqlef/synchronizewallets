from django.contrib import admin
from main.models import Phrase, KeyStore, PrivateKey

# Register your models here.

admin.site.register(Phrase)
admin.site.register(KeyStore)
admin.site.register(PrivateKey)