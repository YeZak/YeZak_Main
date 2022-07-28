from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import  MultiPartParser, FormParser
from django.http import Http404

from .serializers import PostSerializer
from .models import Item

import math
from typing import ItemsView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from urllib.parse import quote

import os
from django.db.models import Q
from django.shortcuts import get_object_or_404
from . import models


#ml
from ml.models import load_default_model, label_str
from ml.CLIP_model import CLIP_tag
from ml.interior import image_merge
from torchvision import transforms
import skimage.io as io
import json
import PIL.Image
from yezak.settings import BASE_DIR

classifier = load_default_model()

transform = transforms.Compose([
    transforms.Resize([256, 256]),
    transforms.ToTensor(),
])

#WEB_PATH = "http://127.0.0.1:8000"

class ItemList(APIView):   #목록 보여줌4
    parser_classes = (MultiPartParser , FormParser)

    def get(self, request, *args, **kwargs):  #리스트 보여줄 때
        items = Item.objects.all()

        serializer = PostSerializer(items, context={"request":request} ,many=True)  #여러개 객체 serialize 하려면 many=True
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):  #새 글 작성시

        serializer = PostSerializer(data=request.data)  # request.data는 사용자 입력 데이터

        if serializer.is_valid():   # 유효성 검사

            img_label = serializer.validated_data['item_pic']
            img_tag = serializer.validated_data['item_pic']
            img_interior = serializer.validated_data['item_pic']

            image = io.imread(img_label)
            pil_image = PIL.Image.fromarray(image)

            pil_image = transform(pil_image)
            pil_image = pil_image.unsqueeze(0)
            #
            prediction = classifier(pil_image)
            prediction_index = prediction.argmax()

            serializer.validated_data["label"] = prediction_index
            serializer.validated_data["prediction"] = label_str(prediction_index)

            # tag
            tag = CLIP_tag(img_tag, Is_path=True)
            serializer.validated_data["tag_list"] = json.dumps(tag)

            #################interior     오류나는부분################

            image_resized, back_img = image_merge(img_interior,prediction_index, Is_path=True)
            serializer.validated_data["pic_interior"] = back_img
            # #######################################
            serializer.save()  # 저장

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            print('error',serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ItemDetail(APIView):
    def get_object(self, pk):  # Item 객체 가져오기
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):  # Item detail 보기
        item = self.get_object(pk)
        serializer = PostSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # Item 수정하기
        item = self.get_object(pk)
        serializer = PostSerializer(item, data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.save()  # 저장
            return ResourceWarning(serializer.data)
        return ResourceWarning(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # Item 삭제하기
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# # django item_detail - 장고랑만 연결함
# def item_detail(request, pk):
#     login_session = request.session.get('login_session','')
#     context = {'login_session':login_session}
#     items = get_object_or_404(Item, item_id=pk)
#     context['items']=items
#     return render(request, 'posts/detail.html', context)

def create(request):
    return render(request, 'posts/upload.html')

def item_upload(request):
    # if request.method == "POST":
    #     # Fetching the form data
    #     item_pic = request.FILES["item_pic"]

    #     # Saving the information in the database
    #     document = models.Item(
    #         item_pic = item_pic
    #     )
    #     document.save()

    # documents = models.Item.objects.all()

    items=Item()
    items.item_name=request.GET['item_name']
    items.details=request.GET['details']
    items.price=request.GET['price']
    items.item_pic = request.POST.get('item_pic', '')
    # items.date= timezone.datetime.now()
    # items.seller=123
    items.item_size_width=request.GET['item_size_width']
    items.item_size_height=request.GET['item_size_height']
    items.save()

    return redirect('../')
    # return render(request, "posts/upload.html", context = {
    #     "files": documents
    # })

# # django item_list
# def item_list(request):
#     try:
#         search_option=request.POST['search_option']   #검색 옵션
#     except:
#         search_option='seller'   #기본 검색 옵션

#     try:
#         search=request.POST['search']    #검색 키워드
#     except:
#         search=''

#         itemCount = Item.objects.count()  #레코드 카운트

#     # #1페이지 [0:10], 2페이지[10,20]
#     # try:
#     #     start=int(request.GET['start'])   #레코드 시작 번호 [start:end]
#     # except:
#     #     start=0

#     # page_size=10 # 한페이지 레코드 수
#     # page_list_size=10 # 페이지 갯수
#     # end=start+page_size
#     # # math.ceil == 올림
#     # total_page=math.ceil(itemCount/page_size) #전체 페이지 갯수
#     # current_page=math.ceil((start+1)/page_size)
#     # # math,floor == 버림
#     # start_page=math.floor((current_page-1)/page_list_size)*page_list_size+1
#     # end_page=start_page+page_list_size-1
#     # if total_page < end_page:
#     #     end_page = total_page
#     # #이전 페이지
#     # if start_page >= page_list_size:
#     #     prev_list=(start_page-2)*page_size
#     # else:
#     #     prev_list=0

#     # #다음 페이지
#     # if total_page>end_page:
#     #     next_list=end_page*page_size
#     # else:
#     #     next_list=0

#     if search_option=='all':
#         itemList=Item.objects.filter(
#             Q(seller__contains=search) | Q(item_name__contains=search) | Q(details__contains=search)
#         ).order_by('-item_id')
#         # [start:end]
#     elif search_option=='seller_id':
#         itemList = Item.objects.filter(
#             Q(seller__contains=search)
#         ).order_by('-item_id')
#         # [start:end]
#     elif search_option=='item_name':
#         itemList = Item.objects.filter(
#             Q(item_name__contains=search)
#         ).order_by('-item_id')
#         # [start:end]
#     elif search_option=='details':
#         itemList = Item.objects.filter(
#             Q(details__contains=search)
#         ).order_by('-item_id')
#         # [start:end]

#     links=[]
#     # for i in range(start_page, end_page + 1):
#     #     page=(i-1)*page_size
#     #     links.append("<a href='?start="+str(page)+"'>"+str(i)+"</a>")

#     itemList=Item.objects.all()
#     return render(request, 'posts/list.html'
#     , {'itemList':itemList, 'itemCount':len(itemList), 'search_option':search_option, 'search':search,
#     # 'range':range(start_page-1, end_page), 'start_page':start_page, 'end_page':end_page,
#     # 'page_list_size':page_list_size, 'total_page':total_page, 'prev_list':prev_list, 'next_list':next_list, 
#     'links':links}    
#     )

def update(request, item_id):
    items = Item.objects.get(item_id=item_id)
    login_session = request.session.get('login_session','')
    context = {'login_session':login_session}
    context['items']=items

    if request.method == "POST":
        items.item_name=request.POST['item_name']
        items.details=request.POST['details']
        items.price=request.POST['price']
        # items.seller=123
        items.item_size_width=request.POST['item_size_width']
        items.item_size_height=request.POST['item_size_height']
        items.save()
        return redirect('../../')

    else:
        return render(request, 'posts/update.html', context)
    # id =request.POST['item_id']
    # row_src=Item.objects.get(item_id=id)

    # fname=row_src.filename
    # fsize=row_src.filesize
    # if 'file' in request.FILES:  # 파일을 첨부한 경우
    #     file=request.FILES['file']
    #     fname=file._name  #파일 이름
    #     #write binary
    #     with open('%s%s' % (UPLOAD_DIR, fname),'wb') as fp:
    #         for chunk in file.chunks():
    #             fp.write(chunk)
    #     fsize=os.path.getsize(UPLOAD_DIR+fname)

    # row_new=Item(item_id=id, seller=request.POST['seller'], item_name=request.POST['item_name'],
    #             details=request.POST['details'])
    # row_new.save()
    # return redirect('/')

def delete(request):
    id=request.POST['item_id']
    Item.objects.get(item_id=id).delete()
    return redirect('/')

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "posts/upload.html", context = {
        "files": documents
    })