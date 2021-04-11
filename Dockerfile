# set base image (host OS)
FROM python:3.8-slim-buster

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local source directory to the working directory in docker that app here
COPY . .

# command to run on container start
#CMD [ "python", "./argparser_python.py","admin" ,"123456" ,"http://127.0.0.1:8880/api/device/get-hostname-by-vpn-id" ,"gethostnamebyvpnid.txtpi"]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# ENTRYPOINT [ "python" ]
CMD [ "python3", "app.py" ]