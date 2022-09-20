from django.shortcuts import render
from mywatchlist.models import watchlistItems
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist_item = watchlistItems.objects.all()
    context = {
        'list_item': data_watchlist_item,
        'name': 'Muhammad Ghazian Gunawan',
        'student_id': '2106656522'
    }

    return render(request, 'watchlist.html',context)



def show_xml(request):
    data = watchlistItems.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = watchlistItems.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    

def show_json_by_id(request, id):
    data = watchlistItems.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

