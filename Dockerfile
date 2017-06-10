FROM python:2.7-alpine
ENV PATH /usr/local/bin:$PATH
ENV PATH /home:$PATH
ADD . /home
WORKDIR /home
RUN apk update && apk add zlib-dev && apk add jpeg-dev && apk add alpine-sdk
RUN pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver

