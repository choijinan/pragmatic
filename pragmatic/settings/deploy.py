from .base import *

env = environ.Env(  # secret key를 위한 설정!!
    # set casting, default value
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env(
    env_file= os.path.join(BASE_DIR, '.env')         # secret key를 위한 설정!!
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # 배포할때는 false여야 수정이 불가능함!!

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {                                 # 위의 링크로 들어가서 아래내용 복사하고 붙여넣기!!
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysql을 쓰는 이유는 mariadb는 mysql의 분기된 db임 그래서 거의 같다고 보면됨!!
        'NAME': 'django',                     # 연결하는 mariadb 안에서 db를 만들것이다. 그 만든 db의 이름이 어떻게 될것인지 설정하는 것이다.
        'USER': 'django',                     # 유저이름 설정인듯
        'PASSWORD': 'wlsdks12',               # 비번설정
        'HOST': 'mariadb',                    # 연결된 컨테이너끼리는 container의 이름을 통해 통신하기때문에 mariadb라는 컨테이너를 만들었으니 이름을 적어주면 연결됨!!
        'PORT': '3306',                       # 연결된 컨테이너끼리는 이름으로 연결이가능!! 127.0.0.1:8000 <= 이 형식이 아니라 도메인형식으로 연결 할수 있게 된다!!
    }                                         # 마리아db, mysql 은 3306번 포트를 사용함!!
}
