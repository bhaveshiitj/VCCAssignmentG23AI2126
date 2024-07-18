Bhavesh - G23AI2126
**Deploy a sample web application using docker containers by creating docker images from scratch. Existing docker container images are not allowed.** 

Steps to follow:-      

1. Build a simple flask application with the file named [app.py](http://app.py) (the file name can be different as well). 
2. Create a requirements.txt file containing all the dependencies that need to be installed to run the application. 
3. Create a docker file. 
4. the docker file should have the following set of commands inside to create an image successfully: 
    
    FROM baseimage( python:3.8-alpine in our case)
    
    COPY . /app
    
    WORKDIR /app 
    
    RUN pip install -r requirements.txt
    
    CMD python app.py
    
5. Open CMD and use the following commands to build a docker image  and run it: 
    
    
    1. docker build -t welcome-app(name of your docker image) . 
    2. docker images ( to check existing images and if the new image is created or not) 
    3. docker run  -p 5000:5000 ( host port and container port) welcome-app

1. docker stop  containerid ( to stop the container ) 
2. Deployment of image in Docker Hub -
    1. Login to Docker Hub
    2. check the image name such that it is named in the following convention : 
        
        username/docker-image-name
        
        to rename simply delete the existing image by the following command - 
        
        docker image rm -f image-name
        
        create new image 
        
        docker build -t username/image-name .
        
    3. use the following command in cmd: 
    
    docker push username/image-name:latest (latest will push the tag with the latest version)
    
    check in docker hub if the image is pushed or not.
    
    1. To pull a docker image use the following command : 
        
        docker pull username/image-name:latest
        
    
    To run the pulled docker image simply use the command : 
    
    docker run -p 5000:5000 username/image-name:latest
