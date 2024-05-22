from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from app1.models import Product,Category,Carts,Orders
from app1.forms import UserRegisterForm,UserLoginForm,CartForm,OrderForm
from django.http import HttpResponse
from django.contrib import messages
# from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail,settings
from django.utils.decorators import method_decorator
from app1.decorators import login_required

# Create your views here.


class HomeView(View):
    def get(self,request):
        products=Product.objects.all()
        return render(request,'index.html',{'products':products})

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        forms=UserRegisterForm()
        return render(request,'user_register.html',{'forms':forms})
    def post(self,request,*args,**kwrags):
        forms=UserRegisterForm(request.POST)
        if forms.is_valid():
            User.objects.create_user(**forms.cleaned_data)
            messages.success(request,"Successfully Registered")
            return redirect('home_view')
        else:
            messages.error(request,"Invalid credentiaals ! Please register again")
            return redirect("reg_view")

class UserLoginView(View):
    def get(self,request,*args,**kwargs):
        form=UserLoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request,*args,**kwrags):
       username=request.POST.get('username')
       psw=request.POST.get('password')
       user=authenticate(request,username=username,password=psw)
       if user:
           login(request,user)
           messages.success(request,'Login succesful')
           return redirect('home_view')
       else:
           messages.error(request,'Invalid credentials')
           return redirect('login_view')
       
@method_decorator(login_required,name="dispatch")       
class UserLogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home_view')

class ProductDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        product=Product.objects.get(id=id)
        return render(request,'product_detailview.html',{'product':product})

@method_decorator(login_required,name="dispatch")  
class AddtoCartView(View):
    def get(self,request,*args,**kwargs):
        forms=CartForm()
        id=kwargs.get("id")
        product=Product.objects.get(id=id)
        return render(request,'carts.html',{'forms':forms,'product':product})
    
    def post(self,request,*args,**kwargs):
        usr=request.user
        id=kwargs.get('id')
        prd=Product.objects.get(id=id)
        q=request.POST.get('quantity')
        Carts.objects.create(user=usr,product=prd,quantity=q)
        return redirect('home_view')

@method_decorator(login_required,name="dispatch")    
class CartListView(View):
    def get(self,request,*args,**kwargs):
        data=Carts.objects.filter(user=request.user).exclude(status='order=placed')
        return render(request,'cartlist.html',{'data':data})
 

class PlaceOrderView(View):
    def get(self,request,*args,**kwargs):
        form=OrderForm()
        return render(request,'orderlist.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        cart_id=kwargs.get('cart_id')
        cart=Carts.objects.get(id=cart_id)
        user=request.user
        address=request.POST.get('address')
        email=request.POST.get('email')
        Orders.objects.create(user=user,cart=cart,address=address,email=email)
        send_mail("confirmation","order placed succesfully",settings.EMAIL_HOST_USER,[email])
        cart.status='order-placed'
        cart.save()
        return redirect('home_view')
    

class OrderDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        data=Carts.objects.get(id=id)
        data.delete()
        return redirect('cartlist_view')






