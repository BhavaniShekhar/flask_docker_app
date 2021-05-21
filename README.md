# flask Docker App

To run this Flask app on Docker container do the following steps

    docker build -t flask:1.0 .

To run the container 
    docker run -d -p 8083:80 -v /home/vagrant/Flask_Docker_App/app:/app  --rm flask:1.0
    
Customized for Learning basics of Flask web applicaiton that runs on a Docker ecosystem.
