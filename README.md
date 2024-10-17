# Ollama Docker FastAPI

This project demonstrates how to set up a Dockerized environment with FastAPI and Ollama using Docker Compose. It includes GPU access through the NVIDIA Docker toolkit to optimize Ollama's performance.

## Prerequisites

Before starting, ensure you have the following installed:

1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker Compose](https://docs.docker.com/compose/install/)
3. [NVIDIA Docker Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) (required for GPU support)

## Getting Started

 **Clone the repository:**

   ```bash
   git clone https://github.com/vishvaRam/OllamaDockerFastAPI.git
   cd OllamaDockerFastAPI
   ```
   ## Set up the NVIDIA Docker Toolkit

Follow the [installation guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) for setting up the NVIDIA Docker Toolkit to access your system's GPU from within Docker containers.

## Prepare the model storage directory

Make sure the directory `/your/local/path/for/model` exists and contains the models required for Ollama.

## Docker Compose Services

The Docker Compose configuration defines two services:

1. **web (FastAPI):**
   - Runs the FastAPI application.
   - Listens on port `8000`.
   - Maps the local `FastAPI` directory to the container’s `/app` directory.
   - Uses the shared network `ollama-net`.
2. **ollama (Ollama Service):**
   - Utilizes the official Ollama image from Docker Hub.
   - Maps the local model directory to the container's `/root/.ollama` directory for model storage and access.
   - Exposes port `11434` for communication.
   - Accesses the GPU using the NVIDIA Docker toolkit with GPU configuration specified in the Compose file.
   - Uses a custom startup script (`/start-ollama.sh`) as the entry point.

## Pulling Different Models from Ollama

The `Ollama/start-ollama.sh` script can be modified to pull any model from Ollama. By default, the script pulls the `llama3.2:1b` model, but you can change it to pull any other model available on Ollama.


## Usage

1. **Build and run the containers:**

   ```bash
   docker-compose up --build
   ```

   This command builds the Docker images and starts the services in the foreground.

2. **Access FastAPI:**

   The FastAPI application will be available at [http://localhost:8000](http://localhost:8000).

3. **Verify Ollama Service:**

   Ensure the Ollama service is accessible at [http://localhost:11434](http://localhost:11434).

## Customizations

- Modify the `docker-compose.yml` file to change ports, volume paths, or other configurations.
- Update the FastAPI application code inside the `FastAPI` directory as needed.

## Troubleshooting

1. **Ollama model directory not found:**

   Ensure that the directory exists and contains the necessary models.

2. **GPU not detected:**

   Make sure the NVIDIA Docker Toolkit is properly installed, and the system has the required drivers for GPU access.

3. **FastAPI not accessible:**

   Verify that port `8000` and `11434` are not already in use on your host machine.

## Clean Up

To stop the services and remove the containers, run:

```bash
docker-compose down
```
To remove the images as well, add the --rmi all flag:

```bash
docker-compose down --rmi all

