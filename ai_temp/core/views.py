from PIL import Image
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView
from torchvision import transforms

from datetime import datetime, timedelta

from core.models import Item
from ml.models import load_default_model
from ml.CLIP_model import CLIP_tag

import skimage.io as io

import simplejson as json


classifier = load_default_model()

transform = transforms.Compose([
    transforms.Resize([256, 256]),
    transforms.ToTensor(),
])


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Item.objects.filter(created__gt= datetime.now() - timedelta(hours = 1)).all()
        return context


class PostCreateView(CreateView):
    template_name = "core/post_create.html"
    success_url = reverse_lazy("home")

    model = Item
    fields = ["image"]

    def form_valid(self, form):
        self.object: Item = form.save(commit=False)
        image = Image.open(self.object.image)
        image.save("image.jpeg")

        image = transform(image)
        image = image.unsqueeze(0)

        prediction = classifier(image)
        prediction_index = prediction.argmax()

        if prediction_index == 0:
            self.object.prediction = Item.ORIENTALISM
        elif prediction_index == 1:
            self.object.prediction = Item.REALISM
        elif prediction_index == 2:
            self.object.prediction = Item.ANIMATION
        elif prediction_index == 3:
            self.object.prediction = Item.PENCIL
        elif prediction_index == 4:
            self.object.prediction = Item.IMPRESSIONISM
        elif prediction_index == 5:
            self.object.prediction = Item.ABSTRACT
        elif prediction_index == 6:
            self.object.prediction = Item.POPART

        #tag
        tag = CLIP_tag("image.jpeg")
        self.object.tag_list = json.dumps(tag)

        self.object.save()

        return super().form_valid(form)



class AppView(TemplateView):
    template_name = "index.html"  # app/build/index.html

class PostListApiView(View):
    def get(self, request, *args, **kwargs):
        posts = Item.objects.all()
        posts = map(lambda post: {
            "id": post.id,
            "prediction": post.prediction,
            "image_url": post.image.url,
        }, posts)
        posts = list(posts)
        return JsonResponse(posts, safe=False)

    def post(self, request, *args, **kwargs):
        return HttpResponseNotFound()


@method_decorator(csrf_exempt, name='dispatch')
class PostCreateApiView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound()

    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")
        if image is None:
            return HttpResponseBadRequest()

        self.object = Item(image=image)
        prediction_index = predict(self.object.image)  # run ml model

        post = Item(image=image)

        if (prediction_index == 0 or prediction_index == 2):
            post.prediction = Item.THEME3
        elif (prediction_index == 1):
            post.prediction = Item.THEME2
        elif (prediction_index == 3):
            post.prediction = Item.THEME5
        elif (prediction_index == 4):
            post.prediction = Item.THEME1
        elif (prediction_index == 5 or prediction_index == 6):
            post.prediction = Item.THEME4

        post.save()

        return JsonResponse({"success": True})














