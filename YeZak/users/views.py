# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# # from django.contrib.auth.models import Member
# from django.views.generic.detail import DetailView
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
# import json
# from django.http  import JsonResponse
# from .serializers import MemberSerializer
# from .models import Member
# from rest_framework.parsers import JSONParser

# from .forms import UserForm

# # def signup(request):
# #     if request.method == "POST":
# #         form = UserForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             username = form.cleaned_data.get('username')
# #             raw_password = form.cleaned_data.get('password1')
# #             user = authenticate(username=username, password=raw_password) #사용자 인증
# #             login(request, user) #로그인
# #             #return redirect('mainweb')
# #             return render(request, 'home/mainweb.html')
# #     else:
# #         form = UserForm()
# #     return render(request, 'users/signup.html', {'form' : form})

# # @csrf_exempt
# # def signup(request):
# #     # signup 함수는 GET 요청인 경우 회원가입 화면을 리턴함
# #     # POST 요청인 경우 화면에서 입력한 데이터로 사용자를 생성함
# #     if request.method == "POST":
# #         form =
# #     template_name = 'login.html'
# #     data = request.POST
# #     if User.objects.filter(user_id= data['id']).exists():
# #         context = {
# #             "result" : "이미 존재하는 아이디입니다."
# #         }
# #         return HttpResponse(json.dumps(context),content_type="application/json")
# #     else :
# #         User.objects.create(
# #             user_id = data['id'] , 
# #             email = data['email'] ,
# #             password = data['password'],
# #         ).save()
# #         context = {
# #             "result" : "회원가입 성공"
# #         }
# #         return HttpResponse(json.dumps(context),content_type="application/json")

# # @csrf_exempt
# # def loginCheck(request):
# #     template_name = 'login.html'
# #     request.session['loginOk'] = False
# #     try:
# #         data = request.POST
# #         inputId = data['id']
# #         inputPassword = data['password']

# #     except KeyError:
# #         context = {
# #             "uid" : "empty",
# #             "upass" : "empty",
# #         }
# #         return render(request,template_name,context)
# #     else : 
# #         if User.objects.filter(user_id= inputId).exists():
# #             getUser = User.objects.get(user_id = inputId)
# #             if getUser.password == inputPassword : 
# #                 request.session['loginOk'] = True
# #                 context = {
# #                     "result" : "로그인 성공"
# #                 }
# #             else :
# #                 request.session['loginOk'] = False
# #                 context = {
# #                     "result" : "비밀번호가 틀렸습니다"
# #                 }
# #         else :
# #             request.session['loginOk'] = False
# #             context = {
# #                 "result" : "존재하지 않는 id입니다"
# #             }
# #         return HttpResponse(json.dumps(context),content_type="application/json")



# @csrf_exempt
# def member_list(request):
#     # 계정 전체 조회
#     if request.method == 'GET':
#         query_set = Member.objects.all()
#         serializer = MemberSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     # 회원가입
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MemberSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def member(request, pk):

#     obj = Member.objects.get(pk=pk)

#     # pk로 특정 계정 조회
#     if request.method == 'GET':
#         serializer = MemberSerializer(obj)
#         return JsonResponse(serializer.data, safe=False)

#     # 계정 수정
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = MemberSerializer(obj, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     # 계정 삭제
#     elif request.method == 'DELETE':
#         obj.delete()
#         return HttpResponse(status=204)


# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         search_email = data['email']
#         obj = Member.objects.get(email=search_email)

#         if data['password'] == obj.password:
#             return HttpResponse(status=200)
#         else:
#             return HttpResponse(status=400)




# # class ProfileView(DetailView):
# #     context_object_name = 'profile_user'
# #     model = Member
# #     template_name = 'users/profile.html'

# # @login_required
# # def profile_page(request, username):
# #     user = get_object_or_404(Member, username=username)
# #     return render(request, 'users/profile.html', {'profile_user': user})