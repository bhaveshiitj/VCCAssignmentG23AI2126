This is a simple web application built using Flask and containerized with Docker. 

To run the application follow the below steps : 

1. Clone the repository  to your local machine. 
2. Create a Docker Image by running the following command: 
    docker build -t welcome-app . 
3. Run the Docer image by running the below command: 
    docker run -p 5000:5000 welcome-app 
