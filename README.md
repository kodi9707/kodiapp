# kodiapp
Short Project 2
Web Application Deployment with Django, Docker, and Jenkins for COMP 314
This project demonstrates the deployment of a simple web application using Python, Django, Docker, and Jenkins.

Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 
Docker
Jenkins

Setup and Installation
Clone the Git Repository:

git clone < Github URL>
Navigate to the Project Directory:

cd webapp
Install Dependencies:

pip install -r requirements.txt
Run the Django Development Server:

python manage.py runserver

Access the Web Application:
Open a web browser and go to http://localhost:8000 to view the homepage with the welcome message. 


Log in to your Jenkins dashboard.

Create a New Jenkins Pipeline Job:
Click on "New Item" on the Jenkins dashboard.

Select "Pipeline" and click "OK".
Configure Pipeline Script:

In the job configuration page, scroll down to the "Pipeline" section.
Select "Pipeline script" from the "Definition" dropdown.

Write a script to define the pipeline stages for building the Docker image and pushing it to Docker Hub.

Click on "Build Now" to run the pipeline.

Once the pipeline starts running, you can monitor its progress on the Jenkins dashboard.
The pipeline will check out the code, build the Docker image, and push it to Docker Hub.

Log in to Docker Hub (https://hub.docker.com) using your credentials.
Navigate to your Docker Hub repository to verify that the image has been pushed successfully.
