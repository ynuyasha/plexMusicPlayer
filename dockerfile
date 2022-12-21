FROM library/python:3.6.9
ARG PLEX_TOKEN="xMhxb2UUfz3sTKJzzsfr"
ARG PLEX_URL="https://93-55-241-1.c55b1e3627714c468562823c2cc30aed.plex.direct:32400"
RUN apt-get update && apt-get -y upgrade && apt-get -y install make g++ bash git libffi-dev python-dev curl
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./ /usr/src/app
RUN pip install -r requirements.txt
EXPOSE 80
EXPOSE 443
