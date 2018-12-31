from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from tierlist.models import Fighter, Tier
from tierlist.serializers import *

class FighterReadView(ListCreateAPIView):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer
    lookup_field = 'name'

@api_view(['GET'])
def list(request):
    data = []
    fighters = Fighter.objects.all()
    serializer = FighterSerializer(data,context={'request':request}, many=True)
    return Response({'data':serializer.data})

@api_view(['GET','POST'])
def fighters_list(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        fighters = Fighter.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(fighters,80)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = FighterSerializer(data,context=\
                                        {'request':request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        return Response({'data':serializer.data, 'count':paginator.count,\
                         'numpages':paginator.num_pages,\
                         'nextlink': '/api/customers/?page='\
                                     + str(nextPage), 'prevlink': '/api/customers/?page='\
                                                                  + str(previousPage)})
    elif request.method == 'POST':
        serializer = FighterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fighters_detail(request):
    try:
        fighters = Fighter.objects.all()
    except Fighter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        dat = []
        for f in fighters:
            dat.append(FighterSerializer(f, context={'request': request}).data)

        return Response(dat)

    elif request.method == 'PUT':
        serializer = FighterSerializer(fighters, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fighters.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    num_fighters = Fighter.objects.all().count()
    num_tiers = Tier.objects.all().count()

    context = {
        'num_fighters': num_fighters,
        'num_tiers':num_tiers,
    }

    return render(request, 'index.html', context=context)