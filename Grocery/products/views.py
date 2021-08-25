import json
from products.serializers import Itemserializer
from django.shortcuts import render,redirect
from django.http.response import HttpResponse,JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
import requests
from products.models import Items



def addproducts(request):
    return render(request,'index1.html')

def view(request):
    dbdata= requests.get("http://127.0.0.1:8000/products/all/").json()
    return render(request,'view.html',{"data":dbdata})

def main(request):
    return render(request,'main.html')

def search_page(request):
    return render(request,'search.html')

def update_page(request):
    return render(request,'updateitem.html')

def delete_page(request):
    return render(request,'Delete.html')


@csrf_exempt
def additem(request):
    if(request.method == "POST"):
        event_serialize = Itemserializer(data = request.POST)
        if(event_serialize.is_valid()):
            event_serialize.save()
            return redirect(view)


@csrf_exempt
def item_all(request):
    if(request.method == "GET"):
        item= Items.objects.all()
        item_serialize = Itemserializer(item, many=True)
        return JsonResponse(item_serialize.data,safe=False, status=status.HTTP_200_OK)


@csrf_exempt
def update(request,id):
    try:
        item = Items.objects.get(id = id)
        if(request.method == "GET"):
            item_serialize = Itemserializer(item) 
            return JsonResponse(item_serialize.data,safe=False)
        
        if(request.method=="DELETE"):
            item.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            itemdata=JSONParser().parse(request)
            item_Serializer=Itemserializer(Items,data=itemdata)
            if(item_Serializer.is_valid()):
                item_Serializer.save()
                return JsonResponse(item_Serializer.data,status=status.HTTP_200_OK)
            else:
                return HttpResponse("Error in seialization")
    except Items.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def search(request):
    try:
        getproduct = request.POST.get("productname")
        getproduct = Items.objects.filter(productname=getproduct)
        product_serialize = Itemserializer(getproduct,many=True)
        return render(request,'search.html',{"data":product_serialize.data})
        # return JsonResponse(product_serialize.data,safe=False,status=status.HTTP_200_OK)
    except Items.DoesNotExist:
        return HttpResponse('Invalid prodeuct name ')
    except:
        return HttpResponse("something went wrong")
        
    
        
@csrf_exempt
def updateapi(request):
    try:
        getproduct = request.POST.get("productname")
        getproduct = Items.objects.filter(productname=getproduct)
        product_serialize = Itemserializer(getproduct,many=True)
        return render(request,'updateitem.html',{"data":product_serialize.data})
    except Items.DoesNotExist:
        return HttpResponse('Invalid prodeuct name ')
    except:
        return HttpResponse("something went wrong")



@csrf_exempt
def update_data(request):
    # getid = request.POST.get("newid")
    getname = request.POST.get("newname")
    getDescription = request.POST.get("newDescription")
    getprice = request.POST.get("newprice")
    getmanufacturer = request.POST.get("newManufacturer")
    getmanufacturingdate = request.POST.get("newmanufacturingdate")
    getexpirydate = request.POST.get("newexpirydate")
    mydata= {"productname":getname,"discription":getDescription,"price":getprice,"manufacturer":getmanufacturer,"manufacturingdate":getmanufacturingdate,"expirydate":getexpirydate}
    jsondata=json.dumps(mydata)
    print(jsondata)
    apilink = "http://127.0.0.1:8000/products/update/"+getname
    requests.put(apilink, data=jsondata)
    return HttpResponse('Data has updated successfully')


@csrf_exempt
def deleteapi(request):
    try:
        getproduct = request.POST.get("productname")
        getproduct = Items.objects.filter(productname=getproduct)
        product_serialize = Itemserializer(getproduct,many=True)
        return render(request,'Delete.html',{"data":product_serialize.data})
    except Items.DoesNotExist:
        return HttpResponse('Invalid prodeuct name ')
    except:
        return HttpResponse("something went wrong")



@csrf_exempt
def delete_data(request): 
    getid = request.POST.get("newid")
    apilink = "http://127.0.0.1:8000/products/update/"+getid
    requests.delete(apilink)
    return HttpResponse('Data has deleted successfully')
