# Installation and Running

Follow these steps to build and run the project:

1. **Clone or Navigate to the Project Directory**:
   Ensure you are in the project directory (`C:\Users\buryy\RiderProjects\SparkPy` or wherever you saved the files).

2. **Build the Docker Image**:
   Run the following command to build the Docker image with a fresh build (no cache):
   ```bash
   docker build -t pyspark-app . --no-cache
   ```

3. **Run the Container**:
   Execute the container to run the PySpark script:
   ```bash
   docker run --rm pyspark-app
   ```
