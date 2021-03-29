FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/choijinan/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=e-4+%o*6u^jq!s*k-$3qlq17#atmmr_pqz58s6yffx746dz2p@" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

