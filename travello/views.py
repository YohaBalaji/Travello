import base64
from django.shortcuts import render
from .models import Destination
from accounts.models import users
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login


# Create your views here.

# def index(request):
#     dests = Destination.objects.all()
#     return render(request, 'index.html',{'dests': dests})

# Display [GET Method]
def index(request):
    if request.method == 'GET':
        objs = Destination.objects.all()
        root = {}

        for nCount, obj in enumerate(objs):
            root[nCount] = {
                'id': obj.id,
                'name': obj.name,
                'Description': obj.desc,
                'price': obj.price,
                'Offer': obj.offer,
            }
            if obj.img:
                root[nCount]['Image'] = obj.img.url
            else:
                root[nCount]['Image'] = None

        return JsonResponse(root)
    return JsonResponse({'error': 'Invalid request method'})


# def index(request):
#     if request.method == 'GET':
#         objs = Destination.objects.all().values()
#     return JsonResponse(objs)

# Create [POST Method]
def post_val(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        price = request.POST.get('price', '')
        img = request.FILES.get('img', '')
        offer = request.POST.get('offer', '')
        auth_header = request.headers.get('Authorization', '')
        username = request.headers.get('username', '')

        if not auth_header and not username:
            return HttpResponse('Unauthorized', status=401)
        if auth_header != '':
            method = auth_header.split(' ')[0]
            encoded_credentials = auth_header.split(' ')[1]
            # BEARER_TOKEN
            if method == 'Bearer':
                try:
                    user = users.objects.get(token=encoded_credentials)
                except Exception as e:
                    return HttpResponse(f'Error : {str(e)}')
            # BASIC_AUTH
            elif method == 'Basic':
                try:
                    credentials = base64.b64decode(encoded_credentials).decode('utf-8').split(':')
                    username = credentials[0]
                    password = credentials[1]
                    user = authenticate(request, username=username, password=password)
                except Exception as e:
                    return HttpResponse(f'Error : {str(e)}')
        # Using API_KEY
        elif username != '':
            try:
                user = users.objects.get(user_name=username)
            except Exception as e:
                return HttpResponse(f'Error : {str(e)}')

        if user is not None:
            try:
                obj = Destination(name=name, desc=desc, price=price, img=img, offer=offer)
                obj.save()
                return HttpResponse("User authenticated successfully,Destination created successfully")
            except Exception as e:
                return HttpResponse(f"Error creating destination: {str(e)}")
        else:
            return HttpResponse('Unauthorized', status=401)
    return HttpResponse("Invalid request method")


def view(request):
    # temp = loader.get_template('index.html')
    dests = Destination.objects.all()
    return HttpResponse(render(request, 'index.html', {'dests': dests}))


# Delete
def delid(request):
    if request.method == 'POST':
        id = request.POST.get('id', '')
        print('ID = ', id)
        try:
            obj = Destination.objects.get(id=id)
            obj.delete()
            return HttpResponse("Destroyed successfully")
        except ObjectDoesNotExist:
            return HttpResponse(f"Invalid ID: {str(id)}")


# Update
def updateByID(request):
    if request.method == 'POST':
        id = request.POST.get('id', '')
        try:
            obj = Destination.objects.get(id=id)
            img = request.FILES.get('img', '')
            obj.img = img
            obj.save()
            return HttpResponse("Image Update successfully")
        except ObjectDoesNotExist:
            return HttpResponse(f'Invalid ID: {str(id)}')

        # if request.GET.get('format') == 'json':
        #     return JsonResponse({'images': img_list})
        # else:
        #     return render(request, 'index.html', {'images': img_list})
