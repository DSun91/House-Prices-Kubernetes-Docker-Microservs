# House Prices Microservices Project

This repository contains an application built using Docker and Kubernetes. The project is composed of several microservices, each responsible for different aspects of the house price prediction process. Built in Python using Flask and SQLite3, the project aims to create a model for predicting house prices based on a dataset. It utilizes a microservices architecture for scalability and modularity, with each service containerized using Docker and orchestrated by Kubernetes.

## Table of Contents

- [Overview](#overview)
- [Microservices Architecture](#microservices-architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Building and Running the Project](#building-and-running-the-project)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Docker Images](#docker-images)
 
## Overview
![Image Description](https://raw.githubusercontent.com/DSun91/House-Prices-Kubernetes-Docker-Microservs/main/AppScheme.png)
The House Prices Microservices Project is designed to predict house prices using various microservices. Each microservice is developed in Python with Flask for API endpoints and SQLite3 for data storage. The services are containerized using Docker and orchestrated using Kubernetes. The microservices interact with each other to provide comprehensive price predictions based on different factors such as location, specifications, and market trends.

## Microservices Architecture

The project currently consists of the following microservices:

- **Main Application (`mainapp`)**: Handles the core logic of the application.
- **House Specifications (`housespecs`)**: Manages house specifications data.
- **Prices Service (`prices`)**: Handles price data and predictions.
- **Geolocation Service (`geoloc`)**: Manages geolocation data for houses.
- **Neighbor Service (`neighbor`)**: Provides data about neighboring properties.
- **Business Insights (`businessinsight`)**: Provides market trends and business insights.

Each microservice is built as a separate Docker container and can be independently deployed and scaled.

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed on your machine. [Install Docker](https://docs.docker.com/get-docker/)
- **Kubernetes**: Set up a local Kubernetes cluster (e.g., using Minikube or Docker Desktop). [Install Minikube](https://minikube.sigs.k8s.io/docs/start/) or [Docker Desktop with Kubernetes](https://docs.docker.com/desktop/kubernetes/)
- **kubectl**: Kubernetes command-line tool for deploying and managing applications on Kubernetes. [Install kubectl](https://kubernetes.io/docs/tasks/tools/)

### Building and Running the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/house-prices-kubernetes-docker-microservs.git
   cd house-prices-kubernetes-docker-microservs
   ```

2. **Build and Start the Docker Containers:**

   ```bash
   docker compose up --build
   ```

3. **Tag the Docker Images:**

   After building the images, tag them to prepare for pushing to Docker Hub:

   ```bash
   docker tag housepriceskubernetes-dockermicroservs-mainappimage <docker_id>/housesprice-mainappimage
   docker tag housepriceskubernetes-dockermicroservs-housespecsimage <docker_id>/housesprice-housespecsimage
   docker tag housepriceskubernetes-dockermicroservs-pricesimage <docker_id>/housesprice-pricesimage
   docker tag housepriceskubernetes-dockermicroservs-geolocimage <docker_id>/housesprice-geolocimage
   docker tag housepriceskubernetes-dockermicroservs-neighborimage <docker_id>/housesprice-neighborimage
   docker tag housepriceskubernetes-dockermicroservs-businessinsightimage <docker_id>/housesprice-businessinsightimage
   ```

4. **Push the Docker Images to Docker Hub:**

   ```bash
   docker push <docker_id>/housesprice-mainappimage
   docker push <docker_id>/housesprice-pricesimage
   docker push <docker_id>/housesprice-housespecsimage
   docker push <docker_id>/housesprice-geolocimage
   docker push <docker_id>/housesprice-neighborimage
   docker push <docker_id>/housesprice-businessinsightimage
   ```

## Kubernetes Deployment

To deploy the microservices to a Kubernetes cluster:

1. **Apply the Kubernetes Deployment Configurations:**

   Deploy the microservices using the provided Kubernetes deployment YAML files:

   ```bash
   kubectl apply -f kubernetes-cluster-deployments.yaml
   kubectl apply -f kubernetes-cluster-services.yaml
   ```

2. **Configure Ingress (Optional):**

   If you are using an ingress controller to manage external access to your services:

   ```bash
   kubectl apply -f kubernetes-cluster-ingress.yaml
   ```

   This will expose the services on specified routes.

## Docker Images

The following Docker images are used in this project and are available on Docker Hub:

- `dsun91/housesprice-mainappimage`
- `dsun91/housesprice-housespecsimage`
- `dsun91/housesprice-pricesimage`
- `dsun91/housesprice-geolocimage`
- `dsun91/housesprice-neighborimage`
- `dsun91/housesprice-businessinsightimage`

You can pull these images directly from Docker Hub if you don't want to build them locally.

 
