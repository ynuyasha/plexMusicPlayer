FROM library/python:3.5.10
ARG PLEX_TOKEN="xMhxb2UUfz3sTKJzzsfr"
ARG PLEX_URL="https://93-55-241-1.c55b1e3627714c468562823c2cc30aed.plex.direct:32400"
RUN apt-get update && apt-get -y install libffi-dev python-dev
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./ /usr/src/app
RUN pip install -r requirements.txt
EXPOSE 80
EXPOSE 443
