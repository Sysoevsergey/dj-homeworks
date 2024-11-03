from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Relationship


class RelationshipInLineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            dictionary = form.cleaned_data
            if not dictionary.get('main'):
                continue
            elif dictionary['main'] is True:
                i += 1
        if i == 0:
            raise ValidationError('Выберите главную тему')
        elif i > 1:
            raise ValidationError('Главной темой может быть только одна')
        return super().clean()

class RelationsInLine(admin.TabularInline):
    model = Relationship
    formset = RelationshipInLineFormset


@admin.register(Article, Tag)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationsInLine]
    save_on_top = True