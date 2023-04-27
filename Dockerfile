FROM python:latest

LABEL maintainer aehr
COPY . /app/
WORKDIR /app

RUN echo 'nameserver 8.8.8.8'>/etc/resolv.conf
RUN pip3 install -r requirements.txt
EXPOSE 7789
VOLUME /app/config
CMD python3 collector.py