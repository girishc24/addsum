from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def members(request):
    return HttpResponse("Hello world!")

class Addsum(APIView):
    def post(self, request):
        numbers = request.data['numbers']
        target = request.data['target']

        new = []

        for i in range(len(numbers)): 
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    new.append([i,j]) 
                   
                    
                    

        context = {'number': numbers,'target': target, 'solution': new}
        return Response(context)