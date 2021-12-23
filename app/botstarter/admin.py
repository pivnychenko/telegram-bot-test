from django.contrib import admin

from .models import Question, Answer, User

admin.site.register(Question)
admin.site.register(Answer)


@admin.register(User)
class AdminUser(admin.ModelAdmin):
	fields = ('chat_id', 'state')
	readonly_fields = ('chat_id',)

