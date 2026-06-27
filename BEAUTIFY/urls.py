"""
URL configuration for BEAUTIFY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from beautyapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.firstindex),
    path('contact', views.secondcontact),
    path('about',views.thirdabout),
    path('services',views.fourthservices),
    path('gallery',views.fifthgallery),
    path('user',views.sixthuserregister),
    # path('userlog',views.userlog),
    path('logout',views.logout),
    # path('login',views.log),
    path('makeupartist',views.seventhmakeupartistregister),
    path('login',views.EIGHTHLOGIN),
    path('logout',views.logout),
    path('userhome',views.userhomes),
    # path('login1',views.artistlogin),
    path('orders',views.artisthome),
    # path('payment/<int:id>',views.paymentdetails),
    # path('adminlogin',views.adminlog),
    path('booking',views.booking),
    path('book', views.availartist),
    # path('booked', views.bookingpages),

    # path('cancel',views.cancels),
    path('admindetails',views.admindetails),
    path('custdet',views.admincustdet),
    path('beautiandetails',views.adminbeautian),
    path('accepted/<int:id>',views.accepting),
    path('rejected/<int:id>',views.rejecting),
    # path('orderpage',views.orderdetails),
    path('accept/<int:id>', views.accept),
    path('reject/<int:id>', views.reject),

    path('addfeedback',views.feedbk),
    path('Vfeedback', views.viewfeedback),
    path('adminviewfeedback', views.adminviewfeedback),

    path('profile', views.viewuprofile),
    path('bp', views.viewmakeupartistprofile),
    # path('addservice', views.addservice),

    path('upuser', views.upuser),
    path('usrup', views.upd),
    path('change', views.changeupsd),
    path('vfeedback',views.showfeedbacks),
    path('comp',views.complaints),
    path('addfeedback', views.feedbacks),

    path('vcusr', views.viewcomplaint),
    path('vcomp', views.viewcomp),

    path('loc',views.location),
    path('viewmakeupartist/<name>',views.viewartists),
    path('adser', views.addservices),
    path('vser', views.vservices),
    path('vserv', views.vser),
    path('delser', views.deleteser),
    path('upser', views.upser),
    path('updser', views.updser),
    path('maprofile', views.maprofile),
    path('gallbyma', views.gallbyma),
    path('galleryu', views.gallbyus),

    path('vphbyma', views.vphbyma),

    path('vbma', views.viewbookmakeupartist),
    path('upma', views.upma),
    path('mupd', views.mupd),
    path('changemapswd', views.changemapswd),

    path('accept', views.accept),
    path('reject', views.reject),
    path('dbp', views.detailsmakeupartist),
    path('vbooking', views.viewappointment),
    path('vconfbyma', views.viewconfbyma),
    path('mawarning', views.mawarning),

    path('warning', views.warning),
    path('canpay', views.canpay),
    path('delbp', views.deletema),
    path('pa', views.pay),
    path('pay/<int:id>', views.payment),
    path('adpay', views.adpayment),
    path('adpaytotl', views.adpaytotal),

    path('bppay', views.mapay),
    path('mapaytot', views.mapaytot),

    path('success', views.success),
    path('forgot',views.forgot_password,name="forgot"),
    path('reset/<token>',views.reset_password,name='reset_password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)