# Use the official Ubuntu LTS as the base image
FROM ubuntu:22.04

# Prevent interactive prompts during apt installs
ARG DEBIAN_FRONTEND=noninteractive

# Install Python 3, pip, and clean up apt caches to keep image small
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      python3 \
      python3-pip \
      python3-venv \
      libnss3-tools \
 && rm -rf /var/lib/apt/lists/* \
 && python3 -m pip install --no-cache-dir --upgrade pip \
 && python3 -m pip install --no-cache-dir Flask 

# Make "python" point to "python3"
RUN ln -sf /usr/bin/python3 /usr/bin/python

# Set your working directory
WORKDIR /server

COPY ./loop-server/* .

COPY ./random.bin .

CMD ["python", "loop_server.py"]
