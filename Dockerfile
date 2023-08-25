FROM python

# Install python requirements
COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt

# Expose the port the application runs on
EXPOSE 8000

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src /app

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
