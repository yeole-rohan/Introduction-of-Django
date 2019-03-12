from django.contrib import admin
from .models import Question,Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    extra = 3
    model= Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Add Your Question here :-", {'fields':['question_text']}),
        ("Date Information :-", {'fields' : ['publication_date'], 'classes' : ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text','publication_date','was_publish_recentaly']
    list_filter = ['publication_date']
    search_fields = ['question_text']
    


admin.site.register(Question, QuestionAdmin)
