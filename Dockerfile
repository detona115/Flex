FROM ubuntu:latest


RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

COPY *.py /code/
COPY requirements.txt /code/

RUN adduser --quiet --disabled-password qtuser

RUN apt update &&                  \
    apt upgrade -y &&              \
    apt dist-upgrade -y &&         \
    apt install -y                 \
        git                        \
        wget                       \
        xvfb                       \
        flex                       \
        dh-make                    \
        debhelper                  \
        checkinstall               \
        fuse                       \
        snapcraft                  \
        bison                      \
        libxcursor-dev             \
        libxcomposite-dev          \
        software-properties-common \
        build-essential            \
        libssl-dev                 \
        libxcb1-dev                \
        libx11-dev                 \
        libgl1-mesa-dev            \
        libudev-dev                \
        python3.8                  \
        python3-pyqt5              \
        python3-pip                \
        python3-psycopg2           \
        python3-requests           \
        nano                     &&\
    apt clean

WORKDIR /code/

