# DevOps Practice Repo

This project is a simple task planner web application built with **Docker**, **Python + Flask**, and **PostgreSQL** on the MIREA course.

## Features

- **Web Interface**: A simple and intuitive interface to add, view, and manage tasks.
- **Persistent Storage**: PostgreSQL database to store tasks and related data.
- **Task Management**: You can add tasks with descriptions and times, mark them as completed, and delete them.
- **Dockerized**: The entire app runs in Docker containers for easy deployment and scalability.
- **CI/CD**: GitHub Actions pipeline for automated testing and deployment.

## Technologies Used

- **Docker**: Containerization of the entire application stack (Flask + PostgreSQL).
- **Flask**: Lightweight Python web framework used to build the application.
- **PostgreSQL**: Relational database for storing tasks data.
- **GitHub Actions**: CI/CD pipeline for testing and deployment.
  
## Requirements

- Docker (latest version)
- Docker Compose

## How to Start the Project

### 1. Clone the repository

```bash
git clone https://github.com/marfetch/DEVOPS.git
cd DEVOPS
```
### 2. Setup with Docker Compose
To get started with the project, you can use Docker Compose to set up and run all the services (Flask and PostgreSQL).
Run the following command to start the containers:
```
docker compose up --build
