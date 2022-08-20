from re import search
from django.shortcuts import render,redirect

#models
from accounts.models import User,Room,Image,Amenities

from django.contrib import auth,messages

#forms
from .forms import addRoom_form, signup_form,imageForm

#filter
from .filters import Filter

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        
        user=auth.authenticate(email=email,password=password)
        
        if user is not None:
            auth.login(request, user)
            
            return redirect('/')
        else:
            messages.info(request,"Credentials invalid")
            return redirect('login')
    else:
        # return render(request,'login.html')
        return redirect('/')
    
def signup(request):
    fm=signup_form()
    print('inside sign view')
    if request.method=="POST":
        print('inside if sign view')
        fm=signup_form(request.POST)
        if fm.is_valid():
            fm.save() 
            return redirect('login')
        else:
            fm=signup_form()        
    return render(request,'signup.html',{'signup_form':fm})

            
    
        
    
def dashboard(request):
    roomInfo=Room.objects.filter(user_id=request.user.id)

    temp=[] 
    for i in roomInfo:
        img=Image.objects.filter(room_id=i.id).first()
        temp.append(img)
     
    data=zip(roomInfo,temp)     
    return render(request,'dashboard.html',{'roomForm':addRoom_form(),'imageForm':imageForm(),'data':data,})

def logout(request):
    auth.logout(request)
    return redirect("/")

def addRoom(request):
   
    if request.method=="POST":
        
        data=addRoom_form(request.POST)
        files=request.FILES.getlist('image')
        if data.is_valid():
            fm=data.save(commit=False)
            fm.user_id=request.user.id
            fm.save()
            for i in files:
                Image.objects.create(room=fm,images=i)
                messages.success(request,'new room added')          
            data.save_m2m()    
    else:
        
        return render(request,'addRoom.html',{'addRoom_form':addRoom_form(),'imageForm':imageForm()})
    
    return render(request,'addRoom.html',{'addRoom_form':addRoom_form(),'imageForm':imageForm()})        

def roomDetails(request,through,pk):
    img=Image.objects.filter(room_id=pk)
    roomData=Room.objects.get(id=pk)
  
    return render(request,'roomDetails.html',{"images":img,"roomData":roomData,'through':through})

def rooms(request):
    rooms=Room.objects.all()
    filter=Filter(request.GET,queryset=rooms)
    rooms=filter.qs
    temp=[] 
    for i in rooms:
        img=Image.objects.filter(room_id=i.id).first()
        temp.append(img)
    data=zip(rooms,temp)
    
    if request.method=="POST":
        city=request.POST['searchQueryInput']
        rooms=Room.objects.filter(city=city)
    
        temp=[] 
        for i in rooms:
            img=Image.objects.filter(room_id=i.id).first()
            temp.append(img)
            data=zip(rooms,temp)      
        return render(request,'rooms.html',{'data':data})
          
    return render(request,'rooms.html',{'data':data,"filter":filter})
