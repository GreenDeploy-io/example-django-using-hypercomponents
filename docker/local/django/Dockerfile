# FROM python:3.8.7-alpine3.12
# FROM python:3.9-slim-buster
# python 3.8.10
# to debug the installed dependencies is /usr/local/lib/python3.8/dist-packages
# allauth/socialaccount/providers/oauth2
# docker-compose -f local.yml run --rm --service-ports django  on one terminal
# then in another go and run docker exec -it <docker-container-id> bash
# another useful one https://www.digitalocean.com/community/tutorials/how-to-use-docker-exec-to-run-commands-in-a-docker-container#conclusion
FROM ubuntu:focal-20221019
# because ubuntu-focal uses python3 for latest python3.9 and pip3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

# needed for universe repository
RUN apt-get install -y software-properties-common

# this is needed for the adding of ppa apt-add-repository
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

# needed for pip3
RUN add-apt-repository universe

# cause everytime add apt-repository need to update to work
RUN apt-get update

RUN apt-get install git -y

RUN apt-get install vim -y

RUN apt-get install python3-pip -y --fix-missing

RUN pip3 install --upgrade pip==22.0.4

#########################################
#
# Tailwind needs
#   node and npm
#     and node needs curl
#########################################

RUN apt-get update

# to install node
RUN apt-get install -y curl

# for getting latest version of node
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash

RUN apt-get install -y --fix-missing \
    # for tailwind and no need to install npm cause node now comes with it prepackaged
    nodejs

RUN npm install -g npm@8.14.0

# End of Tailwind requirement

# for other standard libraries
RUN apt-get install -y --no-install-recommends \
    # psycopg2 dependencies
    libpq-dev gcc python3-dev
    # postgresql \
    # CFFI dependencies: i have no idea what these do but allauth apparently depends on them
    # && apk add libffi-dev py-cffi \
    # because RUST is not new enough for the latest cryptography py package
    # see https://cryptography.io/en/latest/installation.html#alpine
    # see https://github.com/pyca/cryptography/issues/5776#issuecomment-775288041
    # && apk add openssl-dev cargo \
    # for tailwind
    # npm nodejs

RUN rm -rf /var/lib/apt/lists/* && \
    apt-get -y clean

RUN mkdir /code
WORKDIR /code

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip3 install pip-tools
RUN pip-sync /requirements/base.txt /requirements/local.txt

COPY . /code/

# Copy the entrypoint to allow DATABASE_URL available
COPY ./docker/production/django/entrypoint /entrypoint
COPY ./docker/production/django/ /

#########################################
#
# For the smallest possible style.css, Tailwind needs to
#   run install node_modules at /code/theme/static_src
#   and run npm audit fix at /code/theme/static_src
#########################################

RUN cd /code/theme/static_src && /usr/bin/npm install
RUN cd /code/theme/static_src && /usr/bin/npm audit fix

# End of Tailwind

RUN ["chmod", "+x", "/entrypoint"]

# copy out /start-web
# start-web executes `migrate` and `runserver 0.0.0.0:8000`
COPY ./docker/local/django/start-web_django /start-web_django
RUN sed -i 's/\r//' /start-web_django
RUN chmod +x /start-web_django

ENTRYPOINT ["/entrypoint"]