
# Data Engineering and ML Ops Project

This project sets up a comprehensive data engineering and machine learning operations (MLOps) environment using Docker. It integrates various tools and services to create a robust pipeline for data processing, model training, and deployment.

## Table of Contents

- [Data Engineering and ML Ops Project](#data-engineering-and-ml-ops-project)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Components](#components)
  - [Prerequisites](#prerequisites)
  - [Setup and Installation](#setup-and-installation)
  - [Usage](#usage)
  - [Architecture](#architecture)
  - [License](#license)

## Project Overview

This project aims to create a scalable and maintainable infrastructure for data engineering and machine learning workflows. It combines popular tools like Apache Airflow, Apache Spark, MLflow, Kafka, Prometheus, and Grafana to provide a complete solution for data processing, model training, monitoring, and visualization.

## Components

- **Apache Airflow**: Workflow management and scheduling
- **PostgreSQL**: Database for Airflow and MLflow metadata
- **Apache Spark**: Distributed data processing
- **MLflow**: Machine learning lifecycle management
- **Apache Kafka**: Real-time data streaming
- **Prometheus**: Monitoring and alerting
- **Grafana**: Data visualization and dashboards

## Prerequisites

- Docker
- Docker Compose
- Git

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>

2. Environment Setup
- Duplicate the `.env.template` file and rename it to `.env`.
- Open `.env` and replace each placeholder value with your actual credentials.
- Save the `.env` file in the root of the project directory.


3. Build and start the services:
docker compose up -d


## Usage

After starting the services, you can access the following components:

* Airflow Web UI: http://localhost:8080
* Spark Master UI: http://localhost:8081
* MLflow UI: http://localhost:5000
* Prometheus UI: http://localhost:9090
* Grafana Dashboard: http://localhost:3000

## Architecture

The project architecture consists of several interconnected services:

- Airflow: Manages and schedules data pipelines.
- PostgreSQL: Serves as the backend database for Airflow and MLflow.
- Spark: Provides distributed data processing capabilities.
- MLflow: Tracks experiments, manages models, and facilitates deployment.
- Kafka: Enables real-time data streaming between components.
- Prometheus: Collects and stores metrics from various services.
- Grafana: Visualizes metrics and creates dashboards for monitoring.
  
All services are containerized and orchestrated using Docker Compose, ensuring easy deployment and scalability.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Please note that this project incorporates various third-party tools and libraries, each with its own license. These include:

- Apache Airflow (Apache License 2.0)
- PostgreSQL (PostgreSQL License)
- Apache Spark (Apache License 2.0)
- MLflow (Apache License 2.0)
- Apache Kafka (Apache License 2.0)
- Prometheus (Apache License 2.0)
- Grafana (Apache License 2.0)

Users of this project should review and comply with the licenses of these individual components separately. The MIT License applied to this project covers only the original work and configurations created specifically for this data engineering and ML Ops setup.
