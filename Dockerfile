FROM python:3.8.13-alpine3.16
#968557029040.dkr.ecr.ap-southeast-1.amazonaws.com/esollabs/cicd:sh-python-ba4ec63-dirty
RUN apk upgrade -U \
    && apk add --no-cache -u ca-certificates libva-intel-driver mpc1-dev libffi-dev build-base supervisor python3-dev build-base linux-headers pcre-dev curl busybox-extras \
    && rm -rf /tmp/* /var/cache/* 

COPY requirements.txt /
COPY lib/requirements.txt /lib/requirements.txt
RUN pip --no-cache-dir install --upgrade pip setuptools
RUN pip --no-cache-dir install -r /lib/requirements.txt
RUN pip --no-cache-dir install -r requirements.txt
RUN pip --no-cache-dir install "Flask[async]"
COPY . /webapps
WORKDIR /webapps