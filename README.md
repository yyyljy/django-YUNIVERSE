# [yuniverse.me](yuniverse.me)
# Django, AWS EC2 Route53, uWSGI, nginx

## 자주 사용하게 될 명령어
 sudo cp -f /srv/django-YUNIVERSE/.config/nginx/mysite.conf /etc/nginx/sites-available/mysite.conf
 sudo ln -sf /etc/nginx/sites-available/mysite.conf /etc/nginx/sites-enabled/mysite.conf
 sudo systemctl daemon-reload
 sudo systemctl restart uwsgi nginx

## uWSGI, nginx 배포 및 AWS Route53 참고 싸이트

https://nerogarret.tistory.com/

### 해결중인 오류
## 1. 입력 명령어 : pip install -r requirements.txt 

오류 : ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: '/home/ktietz/src/ci/alabaster_1611921544520/work'

발생 원인 : (불확실) python PATH 문제일 가능성이 있다고 함.

해결 방법 : 우선 필수 모듈만 pip 로 직접 설치.

### 해결한 오류
## 1. 입력 명령어 : sudo systemctl restart nginx

오류 : nginx: [emerg] invalid number of arguments in "charset" directive in /etc/nginx/sites-enabled/mysite.conf:5

발생 원인 : 오타(4번 라인 세미콜론 누락)

해결 방법 : 오타 수정
