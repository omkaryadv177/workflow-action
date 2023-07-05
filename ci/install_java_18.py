import os

def install_java_18():
  """Installs Java 18 on macOS."""

  java_download_url = "https://jdk.java.net/18/"
  java_file_name = "jdk-18.tar.gz"
  java_extract_dir = "/tmp/java-18"

  # Download the Java installation file.
  os.system(f"curl -L {java_download_url} -o {java_file_name}")

  # Extract the Java installation file.
  os.system(f"tar -xzf {java_file_name} -C {java_extract_dir}")

  # Set the `JAVA_HOME` environment variable.
  os.environ["JAVA_HOME"] = f"{java_extract_dir}/jdk-18"

  # Verify that Java 18 is installed.
  os.system("java -version")

if __name__ == "__main__":
  install_java_18()
