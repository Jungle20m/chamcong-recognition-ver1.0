FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

WORKDIR /opt/DEPLOY/chamcong/chamcong-recognition-ver1.0
# timezone
RUN     apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \ 
        tzdata \
        rsyslog \
        ntp \
        bash \
        htop \ 
        atop \
        vim \
        wget \
        rsync \
        mlocate \
        collectd \
        ca-certificates \
        logwatch
# python, pip
RUN     apt-get install -y \
        vim \
        libsm6 \
        libxext6 \
        libxrender-dev \
        python3-dev \
        python3-pip
#        /bin/rm -rf /var/lib/apt/lists/*
RUN     pip3 install --upgrade pip
COPY    requirements.txt /opt/DEPLOY/chamcong/chamcong-recognition-ver1.0
RUN     pip install -r requirements.txt
# CMD     ["/usr/bin/python3", "main.py"]
