# Use official Python image
FROM python:3.14-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into container
COPY . .

# Install Flask
RUN pip install flask

# Tell Docker which port the app runs on
EXPOSE 5000

# Run the app
CMD ["python3", "main.py"]