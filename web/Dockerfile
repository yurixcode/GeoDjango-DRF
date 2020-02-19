# Python3
# postgresql-cliente
# dependencias de geodjango, como GDAL
FROM makinacorpus/geodjango:bionic-3.6

RUN mkdir -p /data/web
WORKDIR /data/web
COPY requirements.txt /data/web/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /data/web/
RUN mkdir -p gisdrf/static/admin