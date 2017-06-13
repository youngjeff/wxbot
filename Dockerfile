FROM docker.dcos.demo01.nlabs.sg/basewx
ENV PATH /usr/local/bin:$PATH
ENV PATH /home:$PATH
ENV LANG=C.UTF-8
ADD . /home
WORKDIR /home
EXPOSE 8000
CMD python manage.py runserver 0:8000
