from django.shortcuts import render
import torch
from PIL import Image as im
from django import template
from django.contrib import messages
from .models import FlowerModel, ModelPosting
from .forms import FlowerUpload, FormUmum
from django.views.generic import DetailView, ListView
import io
def FlowerLanding(request):
    
    form = FlowerUpload(request.POST, request.FILES)
    if form.is_valid():
        img = request.FILES.get('image')
        img_instance = FlowerModel(
            image=img
        )
        img_instance.save() #titik upload

        img_terbaru = FlowerModel.objects.filter().last() #untuk mengambil objek paling akhir
        img_bytes = img_terbaru.image.read()
        img = im.open(io.BytesIO(img_bytes))


        path_hubconfig = "static/yolov5"
        path_weightfile = "static/bunga/best.pt" #hasil training
        model = torch.hub.load(path_hubconfig, 'custom',
                             path=path_weightfile, source='local')
        results = model(img, size=640)
        
        results.render()
        for img in results.imgs:
            img_base64 = im.fromarray(img)
            img_base64.save("media/yolo_out/def_flower.jpg", format="JPEG")

        hasil_predict_img = "/media/yolo_out/def_flower.jpg"

        form = FlowerUpload()
        context = {
            "bunga": form,
            "flower": hasil_predict_img
        }
        return render(request, 'flower/Orbit.html', context)

    else:
        form = FlowerUpload()
    context = {
        "bunga": form
    }
    return render(request, 'flower/Orbit.html', context)

def Umum(request):
    form = FormUmum(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return render(request,'flower/Orbit.html', {'bunga':form})


class UmumList(ListView):
    model = ModelPosting
    template_name = 'flower/kosong.html'
# Create your views here.
