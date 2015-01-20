FROM ubuntu:trusty
 
#install syslibs needed
RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install libssl-dev libffi-dev swig python-dev python-pip curl git sqlite3 libpq-dev -y
 
# mount the current project workspace under /project inside the container
ADD . /project

RUN mkdir /src

RUN pip install --upgrade pip

# install pip dependencies!
RUN pip install -r /project/requirements.txt

 
WORKDIR /project
#CMD pip install -r /project/requirements.txt && python setup.py nosetests --with-xunit  --traverse-namespace --with-coverage --cover-package=awfm --cover-html -v test
 
CMD pip install -r /project/requirements.txt && pylint --rcfile=standard.rc skype_controller >> pylint.log

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
