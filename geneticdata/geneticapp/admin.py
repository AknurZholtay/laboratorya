from django.contrib import admin
from .models import CustomUser, AnalysisResult

admin.site.register(CustomUser)
admin.site.register(AnalysisResult)


