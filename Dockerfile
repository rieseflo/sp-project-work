# Use a Python base image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the Jupiter Notebook file and any other necessary files
COPY asteroids.ipynb /app/

# Install the required dependencies
RUN pip install jupyter

# Expose the Jupyter Notebook port
EXPOSE 8888

# Run the Jupyter Notebook server when the container starts
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
