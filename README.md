bnvsrnd/dj_ex 리퍼지토리 생성
제어판 > 사용자 계정 > 윈도우 자격증명 관리 > git:https://github.com 편집 
사용자 이름, 암호(personal access tokens) 편집

[ 08/11 ]
index.html 파일 생성 - start bootstrap free template 활용

파이썬 가상환경 설정
python -m venv myenv

가상환경 진입
myenv\Scripts\activate

라이브러리 설치
pip install -r requirements.txt

장고 작업
프로젝트 생성 : django-admin startproject hmkd .
서버 접속 : python manage.py runserver
앱 만들기 : python manage.py startapp home > > settings.py 에 등록
DB 생성 : python manage.py migrate

[ 08/14 ]

관리자 생성 : python manage.py createsuperuser
home 앱 urls.py 생성 및 hmkd.urls.py 세팅


python manage.py createsuperuser
앱 만들기 : python manage.py startapp blog > settings.py 에 등록
blog app urls.py, views.py 코딩 > models.py에서 테이블 생성 > makemigrations > migrate

admin에 모델(Post) 등록 > python manage.py runserver > Posts에 입력



