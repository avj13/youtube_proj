FROM python:3.9

# setup environment variable  
ENV DockerHOME=/home/app/youtube_api  

# create root directory for our project in the container
RUN mkdir -p $DockerHOME 

# Set the working directory to /youtube_api
WORKDIR $DockerHOME 

# Copy the current directory contents into the container at /youtube_api
COPY . $DockerHOME  

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# port where the Django app runs  
EXPOSE 8000  

# start server  
CMD python manage.py runserver 