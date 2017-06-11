FROM docker.io/thiagofalcao/python2.7
ENV PATH /usr/local/bin:$PATH
ENV PATH /home:$PATH
ENV LANG=C.UTF-8
ADD . /home
WORKDIR /home
RUN apt-get update
RUN apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
RUN pip install pyopenssl ndg-httpsclient pyasn1
RUN pip install -r requirements.txt
RUN pip install --upgrade requests
EXPOSE 8000
CMD python manage.py runserver 0:8000
