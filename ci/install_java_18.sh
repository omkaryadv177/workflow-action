#!/bin/bash

java_download_url="https://jdk.java.net/18/"
java_file_name="jdk-18.tar.gz"
java_extract_dir="/tmp/java-18"

# Download the Java installation file
curl -L "$java_download_url" -o "$java_file_name"

# Extract the Java installation file
mkdir -p "$java_extract_dir"
pax -r -f "$java_file_name" -s ',^\.,'"$java_extract_dir"','

# Set the JAVA_HOME environment variable
export JAVA_HOME="$java_extract_dir/jdk-18"

# Add JAVA_HOME to the system PATH
echo 'export JAVA_HOME="$JAVA_HOME"' >> ~/.bash_profile
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile

# Verify that Java 18 is installed
java -version
