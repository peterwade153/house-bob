from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from properties.models import Property


def index(request):
  property_list =  Property.objects.all().order_by('id')
  page = request.GET.get('page', 1)

  paginator = Paginator(property_list, 8)

  try:
    properties = paginator.page(page)
  except PageNotAnInteger:
    properties = paginator.page(1)
  except EmptyPage:
    properties = paginator.page(paginator.num_pages)

  return render(request, 'index.html', {'properties': properties})
