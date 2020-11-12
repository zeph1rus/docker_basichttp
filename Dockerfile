FROM python:3-alpine

LABEL Description="Test HTTP Web Server App" Vendor="github.com/zeph1rus" Version="0.1.5"
WORKDIR /usr/src/app

COPY dock_http.py ./
EXPOSE 8086/tcp
CMD [ "python", "./dock_http.py" ]
