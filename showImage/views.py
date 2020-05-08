from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

def index(request,image_id):
    try:
        image = Image.objects.get(pk=image_id)
        print(image)
    except Image.DoesNotExist:
        raise Http404("image does not exist")
    return render(request, 'showImage/index.html', {'image': image})

