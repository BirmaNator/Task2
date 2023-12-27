# Punchline WebApp

This is a simple Flask app that returns a punchline and an ID.

## Running Inside a Docker Container

To run this application inside a Docker container, follow these steps:

1. **Build the Docker Image**

    First, build the Docker image using the provided `Dockerfile`. Open a terminal in the project directory and run:

    ```bash
    docker build -t punchline-webapp .
    ```

    This command will create a Docker image named `punchline-webapp`.

2. **Run the Docker Container**

    Once the image is built, start a container from this image:

    ```bash
    docker run -p 5000:5000 punchline-webapp
    ```

    This command runs the container and maps port 5000 of the container to port 5000 on your host machine.

3. **Access the Application**

    The Flask application is now running inside the Docker container and is accessible via:

    ```
    http://localhost:5000
    ```

    Open this URL in your web browser to interact with the application.
