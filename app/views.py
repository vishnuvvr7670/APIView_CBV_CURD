from django.shortcuts import render

# Create your views here.
from app.serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response

class ProductCurd(APIView):
    def get(self,request,id):
        PDO=Product.objects.all() #orm
        #PDO=Product.objects.get(id=id)
        PJO=ProductSerializer(PDO,many=True) #json
        return Response(PJO.data)
    
    def post(self,request,id):
        JDO=request.data
        PDO=ProductSerializer(data=JDO)

        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is Inserted SuccessFully'})
        else:
            return Response({'Error':'Data Not Inserted'})
        
    def put(self,request,id):
        PO=Product.objects.get(id=id)
        JDO=ProductSerializer(PO,data=request.data)

        if JDO.is_valid():
            JDO.save()
            return Response({'Update':'Data is Updated SuccessFully'})
        else:
            return Response({'Error':'data not Updated'})
        
    def patch(self,request,id):
        PO=Product.objects.get(id=id)
        JDO=ProductSerializer(PO,data=request.data,partial=True)

        if JDO.is_valid():
            JDO.save()
            return Response({'Update':'Data is Updated SuccessFully'})
        else:
            return Response({'Error':'data not Updated'})
        
    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'delete':'Data Is Deleted..'})

    









        
    