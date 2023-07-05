import os
import shutil
import subprocess
import tarfile

def install_java_18():
    """Installs Java 18 on macOS."""

    java_download_url = "https://jdk.java.net/18/"
    java_file_name = "jdk-18.tar.gz"
    java_extract_dir = "/tmp/java-18"

    # Download the Java installation file.
    subprocess.call(["curl", "-L", "-o", java_file_name, java_download_url])

    # Extract the Java installation file.
    with tarfile.open(java_file_name, "r:gz") as tar:
        tar.extractall(path=java_extract_dir)

    # Set the `JAVA_HOME` environment variable.
    os.environ["JAVA_HOME"] = os.path.join(java_extract_dir, "jdk-18")

    # Verify that Java 18 is installed.
    os.system("java -version")

if __name__ == "__main__":
    install_java_18()
