FROM python:3.10.2-alpine3.15
ENV PYTHONUNBUFFERED=1

#Dependencies installation
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#GCC for alpine
RUN apk add build-base==0.5-r2

#Non root user setted
ENV PATH="/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/metrobus_location_api/.local/bin"
RUN adduser -SD -u 1000 metrobus_location_api
USER metrobus_location_api
WORKDIR /home/metrobus_location_api/metrobus_project

