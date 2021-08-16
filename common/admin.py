from django.contrib import admin

from accounts.models import Users


admin.site.register(Users, )

admin.site.site_header = "ТК Гарант - Логистика"
