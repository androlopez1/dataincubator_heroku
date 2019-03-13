# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Image
from .forms import UploadImageForm

def image_upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image(img=request.FILES['img'])
            image.save()
            return render(request, 'dataincubator/image.html',
                          {'image' : image})
    else:
        form = UploadImageForm()
    return render(request, 'dataincubator/image_upload.html',
                  {'form': form })


