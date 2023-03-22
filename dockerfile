FROM python   
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 5000

# FROM python -- This line specifies that the base image for this Docker image is the official Python image from Docker Hub.
# WORKDIR /app: This sets the working directory for subsequent commands to /app.
# COPY . . : This copies the contents of the current directory (the . on the left-hand side) to the /app directory inside the Docker image (the . on the right-hand side).
# RUN pip install -r requirements.txt: This runs the pip install command to install the Python packages listed in the requirements.txt file.
# CMD ["python", "app.py"]: This specifies the command that should be run when the container starts. In this case, it runs the python app.py command, which starts the Flask app.
# EXPOSE 5000: This exposes port 5000, which is the default port used by Flask, so that it can be accessed from outside the Docker container.
