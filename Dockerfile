FROM python:3.7.5-buster

# Create the rest of the files
COPY . /pandas-vet
WORKDIR /pandas-vet

# Install required packages
RUN pip install --no-cache-dir -r /pandas-vet/requirements_dev.txt

# Install black manually
# Keeping it out of requirements_dev.txt avoids a predictable Travis failure
RUN pip install black

# Install package in developer mode
RUN pip install -e .
