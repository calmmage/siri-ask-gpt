# Start with the official Python image from the Docker Hub
FROM python:3.11-slim-buster

# Set the working directory in docker
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install poetry and dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Specify the command to run on container start
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 8000


