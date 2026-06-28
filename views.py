from django.shortcuts import render,redirect
from django.contrib import messages
from django. http import HttpResponse
from.models import user
from.models import login
from.models import makeupartist
from.models import service
from.models import PasswordReset
from.models import adpay
from.models import complaint
from.models import appointment
from.models import feedback
from.models import payments
from.models import gallery

import razorpay
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt





def firstindex(request):
    # return HttpResponse("HELLO")
     return render(request,'index1.html')

def secondcontact(request):
    return render(request,'contact.html')

def thirdabout(request):
    return render(request,'about.html')

def fourthservices(request):
    return render(request,'services.html')

def fifthgallery(request):
    return render(request,'gallery.html')

def feedbacks(request):
    return render(request,'feedback.html')

def showfeedbacks(request):
    return render(request,'vfeedback.html')

# def viewuprofile(request):
#
#     if 'uid' in request.session:
#         x = request.session['uid']
#         data = user.objects.filter(username=x)
#         d = makeupartist.objects.all()
#         s = set()
#         for i in d:
#             s.add(i.location)
#             l = list(s)
#         return render(request,'profile.html',{'r':data,'r1':l})
#     else:
#         return render(request,'login.html')

# #user profile
# def viewuprofile(request):
#     if request.method == 'GET':
#         x = request.session['u_id']
#         data = user.objects.filter(USERNAME=x)
#     return render(request, "profile.html", {'data': data})

#to view user
def viewuprofile(re):
    if re.method == 'GET':
        x = re.session['u_id']
        data = user.objects.filter(USERNAME=x)
        return render(re, 'profile.html', {'r': data})
    else:
        return render(re,'login.html')


# def viewmprofile(request):
#     if 'mid' in request.session:
#         x = request.session['mid']
#         data = user.objects.filter(USERNAME=x)
#         return render(request, "artistprofile.html")
#     else:
        # return render(request,'login.html')

#makeupartist profile
def viewmakeupartistprofile(request):
    if request.method == 'GET':
        x = request.session['m_id']
        data = makeupartist.objects.filter(username=x)
    return render(request, "artistprofile.html", {'data': data})

# #user update
# def userup(request):
#     if request.method == 'POST':
#         x = request.POST['username']
#         d = user.objects.filter(USERNAME=x)
#         return render(request, 'userupdate.html', {'r':d})
#     else:
#         return render(request,'userupdate.html')

#user update
def upuser(request):
    if request.method=='POST':
        x=request.POST['username']
        d=user.objects.filter(USERNAME=x)
        return render(request,'userupdate.html',{'r':d})
    else:
        return render(request,'userhome.html')




def upd(request):
    if request.method=='POST':
        a = request.POST['name']
        b = request.POST['age']
        c = int(request.POST['phonenumber'])
        g = request.POST['email']
        y= request.POST['n']
        d=user.objects.filter(USERNAME=y)
        d.update(NAME=a,AGE=b,PHONENUMBER=c,EMAIL=g)
        return render(request,'userhome.html')
    else:
        return render(request,'userhome.html')

    # if request.method == 'POST':
    #     name = request.POST['name']
    #     age = request.POST['age']
    #     username = request.POST['username']
    #     email= request.POST['email']
    #     phonenumber = int(request.POST['phonenumber'])
    #     d = user.objects.filter(USERNAME=username)
    #     d.update(NAME=name,AGE=age,EMAIL=email,PHONENUMBER=phonenumber)
    #     return render(request,'userhome.html')
    # else:
    #     return render(request,'userhome.html')
#change usrpswd
def changeupsd(request):
    if request.method == 'POST':
        u = request.POST['username']
        x = request.POST['oldpassword']
        y = request.POST['newpassword']
        d = login.objects.filter(USERNAME=u)
        d.update(PASSWORD=y)
        return render(request, 'userhome.html')
    else:
        return render(request,'changeupswd.html')

def changemapswd(re):
    if re.method=='POST':
        u=re.POST['n1']
        x=re.POST['n2']
        y=re.POST['n3']
        d=login.objects.filter(USERNAME=u)
        d.update(PASSWORD=y)
        return render(re,'artisthome.html')
    else:
        return render(re,'changemapswd.html')


def sixthuserregister(request):
     if request.method == 'POST':
         name = request.POST['name']
         age = request.POST['age']
         username = request.POST['username']
         password = request.POST['password']
         email = request.POST['email']
         phonenumber = request.POST['phonenumber']
         data = user.objects.create(NAME=name, AGE=age, USERNAME=username, EMAIL=email, PHONENUMBER=phonenumber)
         data.save()
         data1 = login.objects.create(USERNAME=username, PASSWORD=password,STATUS='1')
         data1.save()
         return render(request,'index1.html')
     else:
         return render(request,'user.html')


def seventhmakeupartistregister(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        username = request.POST['username']
        photo = request.POST['photo']
        password = request.POST['password']
        email = request.POST['email']
        license = request.POST['license']
        location = request.POST['location']
        time = request.POST['time']
        # ACTION = request.POST['PENDING']


        data = makeupartist.objects.create(name=name,address=address,phonenumber=phonenumber,username=username,photo=photo,email=email,license=license,location=location,time=time,ACTION="PENDING")
        data.save()
        data1 = login.objects.create(USERNAME=username, PASSWORD=password,STATUS='2')
        data1.save()


        return render(request,'index1.html')

    else:
         return render(request, 'makeupartist.html')


# def addservice(request):
#     if 's_id' in request.session:
#         return render(request,'addservices.html')
#     else:
#         return render(request,'login.html')
def admindetails(request):
    if 'a_id' in request.session:
        return render(request,'adminhomes.html')
    else:
        return render(request,'login.html')

def userhomes(request):
    if 'u_id' in request.session:
        username = request.session['u_id']
        x =user.objects.filter(USERNAME=username)
        y = makeupartist.objects.all()
        s = set()
        for i in y:
            s.add(i.location)
        l = list(s)

        return render(request,'userhome.html',{'r':x,'r1':l})
    else:
        return render(request,login.html)

def artisthome(request):
    if 'm_id' in request.session:
        username = request.session['m_id']
        # y = makeupartist.objiects.filter(username=username)
        return render(request,'artisthome.html')
    else:
        return render(request,"login.html")

def EIGHTHLOGIN(request):
     if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         try:
             print("hi")
             data = login.objects.get(USERNAME=username)
             print(data,"hi")
             if data.PASSWORD == password:
                 if data.STATUS == '1':
                     request.session['u_id'] = username
                     return redirect(userhomes)


                 elif data.STATUS == '2':
                     x = makeupartist.objects.get(username=username)
                     if x.ACTION == 'ACCEPT':
                         request.session['m_id'] = username
                         return redirect(artisthome)
                     else:
                         messages.info(request,'please wait for Approval')
                         return HttpResponse('PLEASE WAIT FOR APPROVAL')
                 else:
                     request.session['a_id']=username
                     return  redirect(admindetails)
             else:
                 return HttpResponse("INCORRECT PASSWORD")

         except Exception:
              return HttpResponse("INCORRECT USERNAME")
     else:
      return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            print("hi")
            data = login.objects.get(USERNAME=username)
            print(data, "hi")
            if data.PASSWORD == password:
                if data.STATUS == '1':
                    request.session.flush['u_id'] = username
                    return redirect(userhomes)
                elif data.STATUS == '2':
                    x = makeupartist.objects.get(USERNAME=username)
                    if x.ACTION == 'Confirm':
                        request.session.flush['m_id'] = username
                        return redirect(artisthome)
                    else:
                        messages.info(request, 'please wait for Approval')
                        return HttpResponse('PLEASE WAIT FOR APPROVAL')
                else:
                    request.session.flush['a_id'] = username
                    return redirect(admindetails)
            else:
                return HttpResponse("INCORRECT PASSWORD")

        except Exception:
            return HttpResponse("INCORRECT USERNAME")
    else:
        return render(request, 'login.html')


#payment
# def payment(re,id):
#     amount = (id+10)*100
#     re.session['amount']=id
#     order_currency = 'INR'
#     client = razorpay.Client(
#         auth=('rzp_test_nwC76q90gEjv8k', 'MvC7NN4DjlyfK7fDATsPqDvj'))
#     # cursor = connection.cursor()
#     # cursor.execute(
#     #     "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(id) + "' ")
#     #
#     # payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
#     return render(re, "payments.html",{'r':amount})



#payment index page
# def paymentdetails(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         name = request.POST['name']
#         addservice = request.POST['addservice']
#         artistname = request.POST['artistname']
#
#
#         data = appointment.objects.create(USERNAME=username,NAME=name,ADDSERVICE=addservice,ARTISTNAME=artistname,ACTION='ACCEPT')
#         data.save()
#
#         if list(data) == []:
#             url = 'vbooking'
#             msg = '''<script>alert('payment not allowed.. your in processing')
#                                 window.location='%s'</script>''' % (url)
#             return HttpResponse(msg)
#         else:
#             data = service.objects.filter(username=username)
#             for i in data:
#                 k = i.amount
#             return render(request, 'paymentindex.html', {'r': data, 'r1': k})
#     else:
#             return redirect(artisthome)
#
    #     return HttpResponse('TRANSACTION SUCCESSFULLY')
    #     # except:
    #     return HttpResponse('TRANSACTION ERROR')
    # #
    #         # return redirect(paymentdetails)
    #
    # else:
    #
    #     return render(request,'payments.html')




# def userhomes(request):
#     return render(request,'userhome.html')


        # return render(request,'adminvmakeupartist.html')


    # data = booking.objects.filter(ACTION="ACCEPT")
    # return render(request, "booking.html", {'data': data})

def availartist(request):
    data = makeupartist.objects.filter(ACTION="ACCEPT")
    return render(request, "adminvmakeupartist.html", {'data': data})


# def cancel(request):
#     data = makeupartist.objects.filter(ACTION="ACCEPT")
#     return render(request, "booking.html", {'data': data})


# def admindetails(request):
#     return render(request,'adminhomes.html')

def admincustdet(request):
    data = user.objects.all()
    return render(request,"custdet.html",{'data':data})

def adminbeautian(request):
    data = makeupartist.objects.filter(ACTION="PENDING")
    return render(request,"beautiandetails.html",{'data':data})

def accepting(request, id):
    makeupartist.objects.filter(id=id).update(ACTION="ACCEPT")
    return redirect(adminbeautian)

def rejecting(request, id):
    makeupartist.objects.filter(id=id).update(ACTION="REJECT")
    return redirect(adminbeautian)

# def orderdetails(request):
#     data = booking.objects.all()
#     return render(request,"orderpage.html",{'data':data})

#
# #reject appointment by beautyparlour
# def reject(re):
#     if re.method=='POST':
#         name = re.POST['name']
#         d=booking.objects.filter(name=name)
#         d.update(action='reject')
#         return HttpResponse('Your Appointment is rejected')
#         # redirect(profile1)
#     else:
#         return render(re,'orders.html')

# def profile(request):
#     if 'uid' in request.session:
#         x = request.session[]

#booking for services
def booking(re):
    if re.method=='POST':
        p=re.POST['a1']
        q = re.POST['b1']
        r = int(re.POST['c1'])
        s = re.POST['d1']
        t = re.POST['e1']
        u = re.POST['service']
        v = re.POST['g1']
        w=re.POST['h1']
        data = appointment.objects.create(name=p,email=q,phone_num=r,booking_date=s,booking_time=t,service=u,username=v,artistname=w,action='pending')

        data.save()
        return redirect(userhomes)
    else:
        x = re.session['mid']
        y=re.session['u_id']
        data = service.objects.filter(username=x)
        return render(re, 'appointment.html', {'r': data,'r1':y})

# def bookings(request):
#         k=request.session['mid']
#         u=request.session['u_id']
#
#         # print(k)
#
#         # email = request.session['email']
#         data1 = user.objects.get(USERNAME=u)
#         data2 = makeupartist.objects.get(username=k)
#         data3 = service.objects.get(username=k)
#
#
#
#         return render(request, "booking.html", {'d1': data1, 'd2': data2,'d3':data3})
#
#
# def bookingpages(request):
#     if request.method == 'POST':
#         username = request.session['u_id']
#         print("hi hlo")
#         name = request.POST['name']
#         useraddress = request.POST['useraddress']
#         useremail = request.POST['email']
#         phonenumber = int(request.POST['phonenumber'])
#         artistname = request.POST['artistname']
#         artistemail = request.POST['artistemail']
#         a = request.POST['a1']
#         # amount = request.POST['amount']
#
#         appointmentdate = datetime.datetime.now()
#         appointmenttime = request.POST['appointmenttime']
#         data = booking.objects.create(USERNAME=username,NAME=name,USERADDRESS=useraddress,USEREMAIL=useremail,PHONENUMBER=phonenumber,ARTISTNAME=artistname,ARTISTEMAIL=artistemail, addservice=a,APPOINTMENTDATE=appointmentdate,APPOINTMENTTIME=appointmenttime,ACTION="PENDING")
#         data.save()
#         # data1 = order.objects.create(USERNAME=username, PHONENUMBER=phonenumber, STATUS='1')
#         # data1.save()
#         return redirect(viewuprofile)
#     # else:
#     #     print('hi')
#     #     x = request.session['sid']
#     #     y = request.session['uid']
#     #     data =service.objects.filter(name=x)
#     #     return render(request, 'booking.html',{'r':data,'r1':y})
#
# # payment index page
# def pay(request):
#     if request.method == 'POST':
#         a = request.POST['a1']
#         b = request.POST['a2']
#         c = request.POST['a3']
#         e=request.POST['a4']
#
#         request.session['u_id']=e
#         request.session['mid']=c
#         d = appointment.objects.filter(username=a,name=e,artistname=c,action='ACCEPT')
#         data = service.objects.filter(addservice=b,name=c)
#         return render(request, 'paymentindex.html',{'r':d,'r1':data})
#     else:
#         return render(request, 'user.html')

        # return render(request, 'payemtindex.html', {'r': d, 'r1': data})

        # if list(d)==[]:
        #     url = 'vbooking'
        #     msg = '''<script>alert('payment not allowed.. your in processing')
        #                     window.location='%s'</script>''' % (url)
        #     return HttpResponse(msg)
        # else:
            # for i in data:
            #     k=i.amount
    # else:
    #     return redirect(userhomes)





def paymentindexs(request):
        u = request.session['u_id']
        data = service.objects.get(username=u)
        return render(request, "paymentpage.html", {'data':data})




    #     return HttpResponse("THANK FOR BOOKING OUR SERVICE."
    #             "YOUR REQUEST HAS BEEN SENT.OUR MAKEUPARTIST WILL GIVE THE REPLAY AS SOON AS POSIBILE WHEATHER ORDER IS TAKEN OR NOT")
    # else:
    #     return render(request, 'adminvmakeupartist.html')

# def cancels(request):
#     if request.method == 'POST':
#         A = request.POST['a1']
#         data = cancel.objects.create(REASONFORCANCELLATION=A)
#         data.save()
#
#         return  HttpResponse('YOUR ORDER HAS BEEN CANCELLED DUE TO YOUR PERSONAL ISSUE')
#     else:
#         return render(request, 'cancelpage.html')

# def complaints(request):
#     if request.method == 'POST':
#
#         name = request.POST['name']
#         username = request.POST['username']
#         email = request.POST['email']
#         phone_number = request.POST['phonenumber']
#         complaint = request.POST['complaint']
#         data = complaints.objects.create(name=name,username=username, email=email,phonenumber=phone_number,complaints=complaint)
#         data.save()
#         return render(request, 'complaint.html')
#     else:
#         a = request.session['u_id']
#         return render(request, 'complaint.html',{'r':a})
#         print("hi")
# def viewcomplaint(request):
#     k = request.session['u_id']
#     b = complaints.objects.filter(username=k)
#     return render(request, 'userviewcomplaint.html', {'r': b})

    # if request.method == 'GET':
    #     data = complaint.objects.all()
    #     return render(request,'userviewcomplaint',{'r':data})
    # else:
    #     return render(request,'adviewcomplaint')

# def addservices(request):
#     if request. method == 'POST':
#         username = request.POST['username']
#         name = request.POST['name']
#         service = request.POST['service']
#         description = request.POST['description']
#         amount = request.POST['amount']

def complaints(request):
    if request.method == 'POST':
        v = request.POST['p1']
        w = request.POST['p2']
        x = request.POST['p3']
        y = request.POST['p4']
        z = request.POST['p5']
        data = complaint.objects.create(username=v,name=w,email=x,phonenumber=y,comp=z)
        data.save()
        return render(request,'userhome.html')
    else:
        a1 = request.session['u_id']
        # data = complaint.objects.filter(username=a1)
        return render(request, 'complaint.html',{'r':a1})


# #complaint by user
# def complaint(request):
#     if request.method == 'POST':
#         v = request.POST['p1']
#         w = request.POST['p2']
#         x = request.POST['p3']
#         y = request.POST['p4']
#         z = request.POST['p5']
#         data=comp.objects.create(username=v,name=w,email=x,phonenumber=y,complaint=z)
#         data.save()
#         return render(request, 'userhome.html')
#     else:
#         a1 = request.session['u_id']
#         return render(request, 'complaint.html',{'r':a1})




#complaint view by admin
def viewcomp(re):
    b = complaint.objects.all()
    return render(re, 'adviewcomplaint.html', {'r': b})


#view complaint by user
def viewcomplaint(re):
    k = re.session['u_id']
    b = complaint.objects.filter(username=k)
    return render(re, 'userviewcomplaint.html',{'r':b})




#user view index page after clicking profile button
def viewartists(request,name):
    request.session['mid']=name
    return render(request,'vmakeupartistindex.html')

def vmakeupindex(request,name):
    if request.method == 'GET':
        x = request.session['mid']
        data = makeupartist.ojects.filter(name=x)
        return render(request,"artist",{'r':data})
    else:
        return render(request,'login.html')


def location(request):
    if request.method == 'POST':
        location = request.POST['location']
        d = makeupartist.objects.filter(location=location,ACTION='ACCEPT')
        return render(request,'viewmakeupartist.html',{'r':d})
    else:
        return render(request,'login.html')

#add service of makeupartist
# def addservices(re):
#     if re.method=='POST':
#         username=re.POST['username']
#         name = re.POST['name']
#         services= re.POST['addservices']
#         description= re.POST['description']
#         amount=int(re.POST['amount'])
#         data = service.objects.create(username=username,name=name,addservice=services,description=description,amount=amount)
#         data.save()
#         return render(re,'artisthome.html')
#     else:
#         x = re.session['mid']
#         data = makeupartist.objects.filter(username=x)
#         return render(re, 'addmakeupservices.html', {'r': data, 'r1': x})


def addservices(re):
    if re.method=='POST':
        username=re.POST['username']
        name = re.POST['name']
        services= re.POST['addservices']
        description= re.POST['description']
        amount=int(re.POST['amount'])
        data = service.objects.create(username=username,name=name,addservice=services,description=description,amount=amount)
        data.save()
        return render(re,'artisthome.html')
    else:
        x = re.session['m_id']
        data = makeupartist.objects.filter(username=x)
        return render(re, 'addmakeupservices.html', {'r': data, 'r1': x})






#delete services
def deleteser(re):
    if re.method=='POST':
        s = re.POST['a1']
        a=re.POST['a2']
        d=service.objects.filter(username=a,addservice=s)
        d.delete()
        return redirect(artisthome)
    else:
        return render(re,'viewservices.html')


#update service
def upser(re):
    if re.method=='POST':
        x=re.POST['c1']
        y=re.POST['c2']
        d=service.objects.filter(username=x,addservice=y)
        return render(re,'upserbyma.html',{'r':d})
    else:
        return render(re,'upserbyma.html')

def updser(re):
    if re.method=='POST':
        a = re.POST['a1']
        b = re.POST['a2']
        c = int(re.POST['a3'])
        e= re.POST['n']
        d=service.objects.filter(username=e,addservice=a)
        d.update(addservice=a,description=b,amount=c)
        return render(re,'artisthome.html')
    else:
        return render(re,'artisthome.html')

#view service of makeupartist
def vservices(request):
    if request.method == 'GET':
        x = request.session['m_id']
        data = service.objects.filter(username=x)
        return render(request, 'viewservice.html', {'data': data})
    else:
        return render(request, 'login.html')

#makeupartist view booking req
def viewbookmakeupartist(request):
    if request.method == 'GET':
        x = request.session['m_id']
        b = makeupartist.objects.get(username=x)
        data = appointment.objects.filter(artistname=b.name,action='pending')
        return render(request, 'vbookingbyma.html', {'r': data})
    else:
        return render(request, 'artisthome.html')

#approve BOOKING by beautyparlour
# def accept(re):
#     if re.method=='POST':
#         username = re.POST['username']
#         email = re.POST['email']
#         name = re.POST['name']
#         d=appointment.objects.filter(username=username,name=name)
#         d.update(action='ACCEPT')
#         send_mail('Confirm Appointment', 'Your Appointment is confirmed','settings.EMAIL_HOST_USER', [email],fail_silently=False)
#         return redirect(artisthome)
#     else:
#         return render(re,'vbookingbyma.html')

#approve BOOKING by beautyparlour

def accept(request, id):
    appointment.objects.filter(id=id).update(action="ACCEPT")
    return redirect(artisthome)

# #reject appointment by beautyparlour

def reject(request, id):
    appointment.objects.filter(id=id).update(action="REJECT")
    return redirect(artisthome)


#
# def reject(re):
#     if re.method=='POST':
#         name = re.POST['a2']
#         d=appointment.objects.filter(name=name)
#         d.update(action='REJECT')
#         return redirect(artisthome)
#     else:
#         return render(re,'vbookingbyma.html')

#view confirmed booking
def viewconfbyma(re):
    if re.method == 'GET':
        c = re.session['m_id']
        b = makeupartist.objects.get(username=c)
        data = appointment.objects.filter(artistname=b,action='ACCEPT')
        return render(re, 'vconfbymakeupartist.html', {'r': data})
    else:
        return render(re, 'artisthome.html')

#user can view ma profile
def detailsmakeupartist(request):
    s=request.session['mid']
    d=makeupartist.objects.filter(username=s)
    return render(request,'makeupartistviewbyusr.html',{'r':d})

#ma can view maprofile
def maprofile(re):
    if re.method == 'GET':
        x = re.session['m_id']
        data = makeupartist.objects.filter(username=x)
        return render(re, 'maprofile.html', {'r': data})
    else:
        return render(re, 'login.html')

#update beauty parlour
def upma(request):
    if request.method=='POST':
        x=request.POST['b1']
        d=makeupartist.objects.filter(username=x)
        return render(request,'updatema.html',{'r':d})
    else:
        return render(request,'updatema.html')

def mupd(re):
    if re.method=='POST':
        a = re.POST['c1']
        # b = re.POST['c2']
        c = re.POST['c3']
        d = int(re.POST['c4'])
        e = re.FILES['c5']
        f = re.FILES['c6']
        g = re.POST['c7']
        i = re.POST['n']
        j=re.POST['c8']
        s=makeupartist.objects.filter(username=i)
        s.update(name=a,address=c,phonenumber=d,photo=e,email=g,license=f,location=j)
        return render(re,'artisthome.html')
    else:
        return render(re,'artisthome.html')


#user viewing their own appointment
def viewappointment(request):
    if request.method == 'GET':
        x = request.session['u_id']
        data = appointment.objects.filter(username=x)
        # print(data)
        return render(request,'viewappointment.html',{'r':data})
    else:
        return render(request,'vbookingbyma.html')

# #view confirmed booking
# def viewconfbyma(request):
#     if request.method =='GET':
#         c = request.session['m_id']
#         m = makeupartist.objects.get(username=c)
#         data = makeupartist.objects.filter(name=m.name,ACTION='ACCEPT')
#         return  render(request,'vconfbymakeupartist.html',{'r':data})
#     else:
#         return render(request,'artisthome.html')


# #user update
# def upuser(request):
#     if request.method=='POST':
#         x=request.POST['c1']
#         d=user.objects.filter(username=x)
#         return render(request,'usrupdate.html',{'r':d})
#     else:
#         return render(request,'usrupdate.html')

#view service by user
def vser(request):
    if request.method == 'GET':
        x = request.session['mid']
        data = service.objects.filter(username=x)
        return render(request, 'viewservicebyuser.html', {'r': data})
    else:
        return render(request, 'login.html')


#admin warning
def warning(re):
    if re.method=='POST':
        name=re.POST['n']
        email=re.POST['n1']
        # d=makeupartist.objects.filter(name=name,email=email)
        send_mail('Warning Message',email,'settings.EMAIL_HOST_USER', [name], fail_silently=False)

        # return render(re, 'adminwarning.html',{'r':d})
        return redirect(admindetails)
    else:
        return render(re, 'adminwarning.html')

def mawarning(re):
    if re.method == 'POST':
        b = re.POST['n']
        c = re.POST['n1']
        send_mail('Warning Message',c,'settings.EMAIL_HOST_USER', [b], fail_silently=False)
        return redirect(admindetails)
    else:
        return render(re,'adminwarning.html')

#cancel/block ma
def deletema(request):
    if request.method=='POST':
        a = request.POST['b1']
        c=request.POST['b2']
        d = makeupartist.objects.filter(name=a,email=c)
        d.delete()
        # send_mail('Rejecting Message', 'You are removed', 'settings.EMAIL_HOST_USER', [c], fail_silently=False)
        return redirect(admindetails)
    else:
        return render(request,'adminvmakeupartist.html')



#

#user cancel payment
def canpay(re):
    if re.method=='POST':
        a = re.POST['c1']
        b = re.POST['c2']
        d = appointment.objects.filter(name=a)
        if b == 'ACCEPT':
            d.update(action='Appointment Cancelled')
            return redirect(userhomes)
        else:
            url = 'vbooking'
            msg = '''<script>alert('Cancel is not possible after payment,no refund')
                                        window.location='%s'</script>''' % (url)
            return HttpResponse(msg)

    else:
        return render(re,'viewappointment.html')

#payment success
# @csrf_exempt
def success(re):
    x= re.session['c_name']
    y=re.session['b_name']
    z=re.session['amount']
    a=appointment.objects.get(name=x)
    b=a.email
    a1=payments.objects.create(NAME=x,ARTISTNAME=y,AMOUNT=z,EMAILID=b)
    a1.save()
    a2=appointment.objects.get (name=x)
    s=a2.username
    a3=adpay.objects.create(username=s,amount=10,artistname=y)
    a3.save()
    a4=appointment.objects.filter(name=x,artistname=y)
    a4.update(ACTION='payment completed')
    return render(re,'userhome.html')

# @csrf_exempt
# def success(request):
#     if request.method == 'POST':
#         c_name = request.POST.get('c_name')
#         b_name = request.POST.get('b_name')
#         amount = request.POST.get('amount')
#
#         if c_name and b_name and amount:
#             return render(request, 'userhome.html')
#         else:
#             return render(request, 'error.html', {'error': 'Missing data in request'})
#     else:
#         return render(request, 'error.html', {'error': 'Invalid request method'})

#admin view their own payment
def adpayment(re):
    a = adpay.objects.all()
    return render(re, 'adminpayment.html', {'r': a})

#admin view total
def adpaytotal(re):
    l=[]
    if re.method=='POST':
        t=re.POST['n1']
        u=adpay.objects.filter(date=t)
        for i in u:
            a=i.amount
            l.append(a)
        s=sum(l)
        return render(re,'adminpayment.html',{'s1':s,'r':u})
    else:
        return render(re,'adminpayment.html')

#view payment by ma
def mapay(request):
        a = request.session['m_id']
        d = makeupartist.objects.get(username=a)
        b = d.name
        d1 = payments.objects.filter(ARTISTNAME=b)
        return render(request, 'makeupartistpayment.html', {'r': d1})

#view payment total by lab
def mapaytot(request):
    l=[]
    if request.method == 'POST':
            a = request.session['m_id']
            v = request.POST['n1']
            d = makeupartist.objects.get(username=a)
            b = d.name
            d1 = payments.objects.filter(ARTISTNAME=b,DATE=v)
            for i in d1:
                a=i.amount
                l.append(a)
            s=sum(l)
            return render(request, 'makeupartistpayment.html',{'s1':s,'r':d1})
    else:
        return render(request,'makeupartistpayment.html')

#forget password
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            u = user.objects.get(email=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=u, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            email('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            # return render(request, 'emailsent.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'forgot.html')

#reset password
def reset_password(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    #usr = User.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            u=password_reset.user.username
            login.objects.filter(username=u).update(password=new_password )
            # password_reset.delete()
            return redirect(login)
    return render(request, 'reset.html',{'token':token})


def feedbk(request):
    if request.method == 'POST':
        v = request.POST['p1']
        w = request.POST['p2']
        x = request.POST['p3']
        y = request.POST['p4']
        z = request.POST['p5']
        data = feedback.objects.create(username=v,name=w,email=x,phonenumber=y,fdbk=z)
        data.save()

        return render(request,'userhome.html')
    else:
        a1 = request.session['u_id']
        # data = feedback.objects.filter(username=a1)
        return render(request, 'feedback.html',{'r':a1})



#view complaint by user
def viewfeedback(re):
    k = re.session['u_id']
    b = feedback.objects.filter(username=k)
    return render(re, 'userviewfeedback.html',{'r':b})

def adminviewfeedback(re):
    k = re.session['u_id']
    b = feedback.objects.filter(username=k)
    return render(re, 'adminviewfeedback.html',{'r':b})

#payment index page
def pay(request):
    if request.method == 'POST':
        a = request.POST['a1']
        b = request.POST['a2']
        # print('b',b)
        c = request.POST['a3']
        e=request.POST['a4']
        request.session['c_name']=e
        request.session['b_name']=c

        d = appointment.objects.filter(username=a,name=e,artistname=c,action='ACCEPT')
        # print(d)
        # k=''
        # m=''
        if list(d)==[]:
            url = 'vbooking'
            msg = '''<script>alert('payment not allowed.. your in processing')
                            window.location='%s'</script>''' % (url)
            return HttpResponse(msg)
        else:
            data = service.objects.filter(addservice=b,name=c)
            # print('data',data)
            # print('addservice,amount',b,c)
            for i in data:

                k=i.amount
                m=i.addservice
                # print(k,m,'hello')
            return render(request, 'paymentindex.html', {'r':d,'r1':k,'r2':m})
    else:
        return redirect(userhomes)

#
# # #user pay
# def payment(request, id):
#         amount = (id+10)*100
#         c_name = 'customer_name'
#         b_name = 'b_name'
#         request.session['amount']=id
#         request.session['c_name'] = 'customer_name'
#         request.session['b_name'] = 'b_name'
#         order_currency = 'INR'
#         client = razorpay.Client(
#             auth=("rzp_test_nwC76q90gEjv8k", "MvC7NN4DjlyfK7fDATsPqDvj"))
#         # cursor = connection.cursor()
#         # cursor.execute(
#         #     "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(
#         #         id) + "' ")
#         payments = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
#         context = {'amount': amount, 'order_currency': order_currency, 'payment': payments, 'c_name': c_name, 'b_name': b_name}
#
#
#         return render(request, "payments.html", context,)

# payment
def payment(re,id):
    amount = (id+10)*100
    re.session['amount']=id
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    # cursor = connection.cursor()
    # cursor.execute(
    # cursor.execute(
    #     "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(id) + "' ")
    #
    # payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return render(re, "pay.html",{'r':amount})

#payment index page
# def pay(request):
#     if request.method == 'POST':
#         a = request.POST['a1']
#         b = request.POST['a2']
#         c = request.POST['a3']
#         e=request.POST['a4']
#         request.session['c_name']=e
#         request.session['b_name']=c
#         d = appointment.objects.filter(username=a,name=e,artistname=c,action='confirm')
#         if list(d)==[]:
#             url = 'vbooking'
#             msg = '''<script>alert('payment not allowed.. your in processing')
#                             window.location='%s'</script>''' % (url)
#             return HttpResponse(msg)
#         else:
#             data = service.objects.filter(service=b,name=c)
#             for i in data:
#                 k=i.amount
#             return render(request, 'paymetindex.html', {'r':d,'r1':k})
#     else:
#         return redirect(userhomes)
#

def gallbyma(re):
    if re.method=='POST':
        a=re.FILES['a1']
        b= re.POST['a2']
        data=gallery.objects.create(photo=a,artistname=b)
        data.save()
        return render(re,'artisthome.html')
    else:
        x = re.session['m_id']
        data = makeupartist.objects.filter(username=x)
        return render(re, 'addphoto.html', {'r': data})

# def gallbyu(re):
#     if re.method=='POST':
#         a=re.FILES['a1']
#         b= re.POST['a2']
#         data=gallery.objects.create(photo=a,artistname=b)
#         data.save()
#         return render(re,'userhome.html')
#     else:
#         x = re.session['u_id']
#         data = makeupartist.objects.filter(username=x)
#         return render(re, 'gallery.html', {'r': data})

#view photo
def vphbyma(re):
    c=re.session['m_id']
    b = makeupartist.objects.get(username=c)
    z=b.name
    a = gallery.objects.filter(artistname=z)
    return render(re, 'viewphoto.html', {'r': a})

def gallbyus(re):
    c=re.session['m_id']
    b = makeupartist.objects.get(username=c)
    z=b.name
    a = gallery.objects.filter(artistname=z)
    return render(re, 'gallery.html', {'r': a})

