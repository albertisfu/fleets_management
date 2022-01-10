### BASE
# The purpose of this image is to prepare the environment, that will
# be used to run the Django stack in the final image.

FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install requirements for compile mysqlclient module
#RUN apt-get_install.sh python3-dev default-libmysqlclient-dev build-essential 

# create the virtual environment for our project
#ENV VIRTUAL_ENV=/venv
#ENV PATH="$VIRTUAL_ENV/bin:$PATH:/docker-bin"

# update pip inside of the virtual environment
RUN pip install --upgrade pip

WORKDIR /webapp

COPY requirements.txt /webapp/requirements.txt

# actually install the requirements into the virtual environment

COPY . /webapp

# run django as development server