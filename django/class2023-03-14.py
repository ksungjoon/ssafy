 # Framework
 # -즉 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은것
 # frame(뼈대,틀)+Work(일하다)
 # -일정한 뼈대, 틀을 가지고 일하다
 # 오늘날 우리가 사용하는 대부분의 웹 서비스는 클라이언트-서버 구조를 기반으로 동작

 # 클라이언트
 # 웹 사용자의 인터네셍 연결된 장치
 # 서비스를 요청하는 주체

 # 서버
 # 웹 페이지,사이트 또는 앱을 저장하는 컴퓨터
 # 요청에 대해 서비스를 응답하는 주체

 # django-  서버를 구현하는 웹 프레임 워크

# 오늘 라이브 ppt 내용
# 1. 바탕화면에 폴더 만들고
# 2. 가상환경 설정하고
# 3. 장고 설치하고 requirement 만들기
# 4. 프로젝트 만들어서
# 5. 서버 실행까지 해보기
#
# ======================================
#
# 프레임 워크란
#
# 즉 서비스 개발에 필요한 기능 (로그인 회원관리 데이터베이스 보안) 등을 미리 구현해서
# 모아 놓은 것 = 프레임워크
# 모든 걸 하나부터 열까지 직접 개발할 필요 없이 미리 만들어 놓은 틀(뼈대)를 사용법에 맞춰
# 골라 쓰기만 하면 됨
#
# cf. 라이브러리 vs 프레임워크
#
# 라이브러리 - 남이 미리 짜 놓은 클래스나 함수들을 모아 놓은 것 필요한 모듈을 가져다 쓰면 됨
#
# 프레임워크 - 웹 서비스 제공하는데 있어 설계의 기반이 되는 뼈대를 제공해 주고 (회원가입 시스템)
#                 그 뼈대에 붙일 일부 코드 까지 제공해 줘서
#                 제공해 준 뼈대에 코드만 잘 제대로 가져다 붙이고
#                 세부적인 기능만 수정해서 사용하도록 제공해 주는 웹 서비스 개발도구
#
# 공통점 : 남들이 만들어 놓은 코드를 사용하는 것. 검증된 코드이기에  SW개발시 빨리 결과를 내 놓을 수 있음
#
# 차이점 : 사용법이 정해져 있는가?
#
#            프레임워크 - 메인 흐름을 프레임워크가 정해 놓아서 그 정해져 있는 흐름을 따라서 코드를 작성
#  		   (메인흐름이 무엇인지 아직 안배웠지만.. 정해져 있는 흐름이 있어 그 흐름에 따라 코드가 작성)
#            라이브러리 - 사용자가 정해놓은 설계에 따라 자유롭게 코드를 작성
#
#
# 장고 장점
#
# 1. 반복적으로 구현해야 하는부분은 이미 만들어져 있다.
# - 로그인, 회원가입, 인증 등 라이브러리가 기본 모듈로 제공된다.
#
# 2. 웹을 만들어야 할때 프론트와 관련된 프레임워크(React, Vue, angular)와 같은것을 사용하지 않고도 만들 수 있다.
# - template에 html을 넣어 연동이 가능하며 특정 조건은 DTL(Django Template Language)를 이용하여 조작이 가능하다.
#
# 3. 데이터베이스 테이블을 models.py에 클래스로 작성하여 작업량을 줄인다.
# - 한번 작업하면 테이블까지 자동 생성되고 매핑도 되기 때문에 편하게 작업이 가능하다.
#
# 따라서 위와같은 기능들로 인해 개발시간이 크게 단축된다.
#
# 장고 단점
# 이미 만들어진 기능을 사용하는 경우가 많기 때문에 원하는대로 커스텀을 하기가 힘들다.
#
#
#
# ================================
#
# 가장 처음 가상환경 부터 생성
# 왜 가상환경부터 생성할까요?
# 강의장에서 작업을 하다가 집 컴퓨터로 작업을 하면 프로젝트 환경이 다를경우 실행이 제대로 안되겠죠?
# 예>집에서 장고3.5 강의장 장고3.2 버전일 경우
# 또는 혼자 프로젝트를 하는것이 아니라 다른 팀원과 프로젝트를 하는데
# 사용하고 있는 개발툴의 버전이 각각 다르면 문제발생 여지가 있다.
# 그래서 가상환경을 생성해서 같은 개발환경으로 셋팅부터 한다.
#
# 가상환경 만들시 주의할점!
# 가상환경을 여러개 만들어 놓았을 경우 이 가상환경이 어떤 프로젝트를 위한 가상환경인지 나중에 헷깔린다.
# 그리고 가상환경이 설치된 폴더가 홈디렉터리에 있는지 바탕화면에 있는지 c드라이브의 어딘가에 있는지 여러개 흩어져 있으면
# 한 폴더가 가상환경 폴더인지 다른 작업을 위한 폴더인지 구분이 잘 안됨!!
# 따라서 가능한 가상환경을 위한 폴더를 하나 만들어 놓고 그 폴더 안에서 관리하는것이 중요하다. !!
#
# 바탕화면에 vscode 바로가기 실행
#
# 홈디렉토리에 venv 라는 가상환경들을 모아놓을 폴더 하나 만들고 그 폴더 안에 first라는 가상환경 하나 만들겠다.
#
# $ cd ~
# $ mkdir venv
# $ cd venv
# $ mkdir first
# $ python -m venv ~/venv/first
# $ source ~/venv/first/Scripts/activate
#
# 가상환경 완성 후
#
# django 설치 (3.2.18 버전 설치)
# autopep8 설치 (들여쓰기 맞춰주는 extention 설치)
#
# $ pip install django==3.2.18
# $ pip install autopep8
# pip list 로 확인
#
# -------------------------------------------------------
# 여기서 잠깐 !!
#
# 다른 컴퓨터에서도 위 프로젝트를 개발시 또는 다른개발자가 위 프로젝트 참여시 개발환경을 같도록 만들어 줘야 하는데
# 위 개발환경과 같도록 하기 위해서 가상환경에 설치된 프로그램과 버전을 저장해 놓을 것이다.
#
# $ pip freeze > requirements.txt
#
# venv폴더 안에 requirements 문서 확인해 보자
# 다른 컴퓨터라고 생각하고 아까만든 first 가상환경은 지우고 새로 해보자
#
# $ deactivate  한 후에 first 지워버리자
#
# 다른 장소 집에 왔다고 생각하고
# 그리고  second라는 폴더만들어서 가상환경셋팅 하자
#
# $ mkdir second
# $ python -m venv ~/venv/second/
# $ source ~/venv/second/Scripts/activate
# $ pip install -r ./requirements.txt
# $ pip list
#
# 자 여기까지 가상환경 환경셋팅이 끝났다.
# 가상환경을 절대절대 깃에 push하지 말자!! 아니 커밋도 하지 말자!!
# 무엇만? requirements 만 올리자 ~~~!!!!!
#
# 이제 django 프레임워크를 사용해서 프로젝트생성하고 일단 서버실행 한번 해 볼 것이다.
# 터미널 경로 이동해보자
# $ cd ~/Desktop
# $ django-admin  startproject firstpjt
# $ cd ./firstpjt
# $ python manage.py runserver
#
#
# 탐색기를 살펴보자 그리고 가상환경도 확인 !!
# $ source ~/venv/second/Scripts/activate
#
#
# settings - 프로젝트 전체적인 설정을 관리 ( 프로젝트 메시지를 한글or영문 / 게시판글올리면 - 기준시간 등등)
#
#
# [urls] - 프로젝트에 대한 URL
# urls - 내가 사용할 앱들의 url을 등록 그 url의 페이지를 요청하면 실행할 Python 코드를 결정
# 예를들면 firstpjt 안에 무비 / 회원관리 / 댓글관리 앱을 만들 것이라면
#
# www.kevin.com/admin
# www.kevin.com/accounts
# www.kevin.com/movies
# www.kevin.com/comments
#
# 각각의 앱에대한 경로를 여기다가 적어 줄 것이다.
#
#
# 1. 자 그러면 이제 앱을 하나 만들어 보자 (앱의 이름은 복수형으로 만드는 것을 권장)
#
# $ python manage.py startapp articles
#
# articles 앱의 구조를 한번 보자
#
# admin.py 은 관리자용 페이지
# models.py 아직은 모르겠지만 나중에 BD에 관련된 내용이 들어갈 것이다.
# 	      회원관리가 있다면 누가 어떤아이디로 어떤비번이고 이메일은 무엇이고 하는 정보를 저장
#
# views.py   각각의 페이지 안에서 실행될 함수 내용이 들어갈 것이다.
#               예를들면 댓글 달 수 있는 게시판을 하나 만들었다면
#              글 생성(create) 글 지우기 (delete) 가 구현이 되는 코드가 들어갈 함수를 적어 줄 것이다
#
#
# 2. 자 그러면 이제 articles앱을 등록을 해보자
#
# setting.py 이동해서
# INSTALLED_APPS > 'articles',  등록하자 (사용자 정의 앱을 가장 위에 순차적으로 적어준다!)
#
# ------------------------------------
# INSTALLED_APPS = [
#     'articles',
#
# ------------------------------------
#
# TIME_ZONE = 'Asia/Seoul'
#
# ------------------------------------
#
#
#
#
# urls.py 이동해서 path 추가해 주자
# ------------------------------------
# from django.contrib import admin
# from django.urls import path
# from articles import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('articles/', views.index),
# ]
# ---------------------------------------
# articles url경로를 적을시 -> views함수 안에있는 index 함수를 호출하겠다!
#
# ---------------------------------------
# view 함수를 적어보자.
#
# def index(request):
#     pass
# ---------------------------------------
# 여기 인덱스 라는 함수에는 화면에 띄울 html문서를 요청 하는 코드가 들어갈 예정이다!!
# 그런데 아직 html 문서를 만들지 않았다 !!
#
# 이 html 문서를 templates 라는 폴더 하나 만들어서
# 거기에 html문서를 작성할 것이다.
# 그리고 나서 index 함수를 통해서 html문서를 요청 할 것이다.
#
# 아티클 안에 templates폴더 하나 만들고
# 거기 안에 articles라는 폴더를 하나 더 만들자
# 그리고 그 안에 index.html이라고 파일하나 생성하자
#
# ---------------------------------------
# <h1>9기 2반 후후훗</h1>
# ---------------------------------------
#
# 그리고 다시 views에 index 함수로 돌아와서
# 웹 문서 요청을 하자
#
# ---------------------------------------
# from django.shortcuts import render
#
# def index(request):
#     return render(request, 'articles/index.html')
# ---------------------------------------
#
# 여기서 중요한 것은 흐름이다.  main stream을 잘 기억 아니 외워야 한다!!
#
# 우리 어떻게 했는가?
#
# 1. 가상환경만들고 django 설치
# 2. requirements 파일 만들고 프로젝트 하나 생성
# 3. 프로젝트 setting에 가서 프로젝트 전반적인 셋팅을 한 후
# 4. 앱 생성 한 후 프로제트 urls에 내가 만들 앱 경로 등록하고
# 5. urls를 통해서 view함수고 호출 될 것이니까 view 함수 만들어주고
# 6. view 함수를 통해서 호출될 템플릿도 만들어 준다
#
# 그렇다면 main stream은 어떻게 되는가?
#
# urls -> view -> template 불러왔다 !
# ★반드시 URL → VIEW → TEMPLATE순으로 코드를 작성한다★
# ====================================== 끝
#
# ------------------------------------------------------------------------------------------------
#
# [참고] 프로젝트 구조
#
# - __init__ : 파이썬이 이 디렉토리를 하나의 패키지로 다루도록 지시. 별도 추가코드 작성X
# - asgi : 장고 앱이 비동기식 웹 서버와 연결, 소통하는 것을 도움. 추후 배포시에 사용
# - settings : 장고 프로젝트 설정 관리
# - urls : 사이트 url과 적절한 views의 연결을 지정
# - wsgi : 장고 앱이 웹서버와 연결, 소통하는 것을 도움. 추후 배포시에 사용
# - manage : 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
#
# → 위에 구조들 중 settings.py와 urls.py만을 직접 수정, 사용 할 것이다 !!
#
# ------------------------------------------------------------------------------------------------
#
# [참고] 어플리케이션 구조
# - admin : 관리자 페이지
# - apps : 앱 정보가 작성된 곳. 별도 추가코드 작성X
# - models : 앱이 사용하는 model 정의. MTV패턴의 M에 해당
# - test : 프로젝트의 테스트 코드를 작성하는 곳
# - views : view함수들이 정의되는 곳 . MTV의 V에 해당
#
# ------------------------------------------------------------------------------------------------
#
# [참고] MTV 디자인 패턴
# Model : 데이터와 관련된 로직 관리 (회원가입 받으면 아이디 비번 이메일 등의 정보를 관리)
# Template : 레이아웃, 화면 처리 (렌더링 하면 화면에 나오는 부분)
# View : model & template과 관련한 로직을 처리해서 응답 반환하는 부분
#
# 만약에
# → www.민호.com/articles ( HTTP  request가 들어오면 )
# → urls.py에서 view 함수 호출 ( view.articles 를 호출한다)
# → view 함수에서는 데이터가 필요하면 model에 접근해서 데이터를 get 하고
# → template을 통해서 화면을 구성
# → 구성된 화면을 응답으로 만들어 클라이언트에게 반환
#
# ------------------------------------------------------------------------------------------------