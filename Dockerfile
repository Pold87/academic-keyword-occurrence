FROM python:3

RUN pip install bs4
RUN pip install urllib5
RUN pip install http3


WORKDIR /data
