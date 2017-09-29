# Base image
FROM alpine:3.5

# Working directory
WORKDIR /src

# Copy app to the Docker container
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY buzz buzz

# Commands to run to install dependencies
RUN apk add --update python py-pip
RUN pip install -r /src/requirements.txt

# Command to run when the container starts
CMD python /src/app.py