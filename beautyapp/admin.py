from django.contrib import admin

from.models import user
admin.site.register(user)

from.models import makeupartist
admin.site.register(makeupartist)

from.models import payments
admin.site.register(payments)

from.models import login
admin.site.register(login)


from.models import booking
admin.site.register(booking)

from.models import appointment
admin.site.register(appointment)

# from.models import cancel
# admin.site.register(cancel)

# from.models import order
# admin.site.register(order)

from.models import PasswordReset
admin.site.register(PasswordReset)

from.models import adpay
admin.site.register(adpay)


from.models import complaint
admin.site.register(complaint)


from.models import service
admin.site.register(service)

from.models import feedback
admin.site.register(feedback)


from.models import gallery
admin.site.register(gallery)


