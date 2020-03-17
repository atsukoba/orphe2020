FROM python:3

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
    python-pip \
    bluetooth \
    bluez \ 
    libbluetooth-dev \ 
    libudev-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
