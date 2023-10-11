# Base image
FROM python:3-slim


# working directory
WORKDIR /app

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrading pip
RUN pip install --upgrade pip 

# copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the project files
COPY . .

# Expose the server port
EXPOSE 8000

# Command to start the server
CMD ["py", "manage.py", "runserver", "0.0.0.0:8080"]