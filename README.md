# flask Docker App

To run this Flask app on Docker container do the following steps

    docker build -t flask:1.0 .
    
        $ docker build -t flask:1.0 .
    Sending build context to Docker daemon  10.24kB
    Step 1/6 : FROM python:3.8-slim-buster
    3.8-slim-buster: Pulling from library/python
    69692152171a: Pull complete 
    66a3c154490a: Pull complete 
    3e35bdfb65b2: Pull complete 
    f2c4c4355073: Pull complete 
    21bb8d414880: Pull complete 
    Digest: sha256:1156cbb1f6a7660dcce3e2f3906a149427fbee71aea0b49953bccf0cc7a3bcaa
    Status: Downloaded newer image for python:3.8-slim-buster
    ---> 40663d3c7bf7
    Step 2/6 : WORKDIR /app
    ---> Running in 9c3c9541f0cc
    Removing intermediate container 9c3c9541f0cc
    ---> 5ee83dc29856
    Step 3/6 : COPY requirements.txt requirements.txt
    ---> 1866b87df891
    Step 4/6 : RUN pip install -r requirements.txt
    ---> Running in fd71ffb0603f
    Collecting json2==0.4.0
    Downloading json2-0.4.0-py3-none-any.whl (2.4 kB)
    Collecting requests==2.23.0
    Downloading requests-2.23.0-py2.py3-none-any.whl (58 kB)
    Collecting Flask==1.1.1
    Downloading Flask-1.1.1-py2.py3-none-any.whl (94 kB)
    Collecting idna<3,>=2.5
    Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
    Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
    Downloading urllib3-1.25.11-py2.py3-none-any.whl (127 kB)
    Collecting certifi>=2017.4.17
    Downloading certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
    Collecting chardet<4,>=3.0.2
    Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
    Collecting itsdangerous>=0.24
    Downloading itsdangerous-2.0.1-py3-none-any.whl (18 kB)
    Collecting Jinja2>=2.10.1
    Downloading Jinja2-3.0.1-py3-none-any.whl (133 kB)
    Collecting click>=5.1
    Downloading click-8.0.1-py3-none-any.whl (97 kB)
    Collecting Werkzeug>=0.15
    Downloading Werkzeug-2.0.1-py3-none-any.whl (288 kB)
    Collecting MarkupSafe>=2.0
    Downloading MarkupSafe-2.0.1-cp38-cp38-manylinux2010_x86_64.whl (30 kB)
    Installing collected packages: MarkupSafe, Werkzeug, urllib3, Jinja2, itsdangerous, idna, click, chardet, certifi, requests, json2, Flask
    Successfully installed Flask-1.1.1 Jinja2-3.0.1 MarkupSafe-2.0.1 Werkzeug-2.0.1 certifi-2020.12.5 chardet-3.0.4 click-8.0.1 idna-2.10 itsdangerous-2.0.1 json2-0.4.0 requests-2.23.0 urllib3-1.25.11
    WARNING: Running pip as root will break packages and permissions. You should install packages reliably by using venv: https://pip.pypa.io/warnings/venv
    Removing intermediate container fd71ffb0603f
    ---> 6999fc4a268b
    Step 5/6 : COPY . .
    ---> fcd7a0c843b8
    Step 6/6 : CMD [ "python3", "app.py" ]
    ---> Running in dda97eff0f34
    Removing intermediate container dda97eff0f34
    ---> b76c49e645af
    Successfully built b76c49e645af
    Successfully tagged flask:1.0

To confirm the image 

    $ docker images
    REPOSITORY   TAG               IMAGE ID       CREATED         SIZE
    flask        1.0               b76c49e645af   3 minutes ago   128MB
    python       3.8-slim-buster   40663d3c7bf7   8 days ago      114MB


To run the container 

    docker run -d -p 8083:80 -v /home/vagrant/Flask_Docker_App/app:/app  --rm flask:1.0
    
Customized for Learning basics of Flask web applicaiton that runs on a Docker ecosystem.
