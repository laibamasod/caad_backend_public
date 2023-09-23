# Use an official Python runtime as the base image
FROM python:3.10-slim

# Update and upgrade libraries, and remove apt cache
RUN apt-get clean all && apt-get update && apt-get upgrade -y && apt-get install make libaio1 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install required packages
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev freetds-dev odbcinst

# Configure ODBC driver
RUN echo "[ODBC Driver 17 for SQL Server]" >> /etc/odbcinst.ini && \
    echo "Description=Microsoft ODBC Driver 17 for SQL Server" >> /etc/odbcinst.ini && \
    echo "Driver=/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so" >> /etc/odbcinst.ini && \
    echo "UsageCount=1" >> /etc/odbcinst.ini
RUN odbcinst -j 
RUN cat /etc/odbcinst.ini

# Create a new user and group
RUN groupadd -r caad && useradd -r -g caad caad

WORKDIR /home/caad
# Copy the requirements file to the working directory

COPY . .

# Update pip without caching anything
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt 

# Set ownership of the working directory to the new user
RUN chown -R caad:caad /home/caad


# Switch to the new user
USER caad

# Set environment variables (modify as needed)a
#ENV DJANGO_SETTINGS_MODULE=icms_teams.settings
#ENV PYTHONUNBUFFERED=1

# Expose the port on which the Django app will run (modify if needed)
EXPOSE 8000/tcp

# Run the Django development server when the container starts


# Set the entrypoint to execute "make" with arguments
ENTRYPOINT ["make"]

# Set the default command to "run"
CMD ["run-gunicorn"]