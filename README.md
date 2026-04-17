# CI/CD Pipeline with GitHub Actions, Docker, AWS ECR, and EC2

A practical CI/CD project that automates the build, push, and deployment of a Dockerized Flask API using **GitHub Actions**, **Amazon ECR**, and **Amazon EC2**.

---

## Project Overview

This project demonstrates how to:

- containerize a Flask app with Docker
- push Docker images to Amazon ECR
- deploy the app on an EC2 instance
- automate deployment with GitHub Actions
- use IAM OIDC authentication instead of long-term AWS keys
- version Docker images with commit SHA tags

---

## Tech Stack

- Python
- Flask
- Docker
- GitHub Actions
- AWS ECR
- AWS EC2
- AWS IAM
- OIDC authentication

---

## Architecture

```text
Developer Pushes Code to GitHub
            |
            v
    GitHub Actions Workflow
            |
            v
      Build Docker Image
            |
            v
       Push Image to ECR
            |
            v
   SSH Into EC2 Automatically
            |
            v
 Pull New Image from Amazon ECR
            |
            v
 Stop Old Container and Run New One
```

---

## Project Structure

```text
CICD-pipeline/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── app.py
├── main.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .dockerignore
```

---

## API Endpoints

Base URL:

```text
http://34.245.120.71
```

Available endpoints:

### 1. Root Endpoint

```text
GET /
```

Response:

```json
{
  "message": "Welcome to Deployment Tracker API",
  "status": "running"
}
```

### 2. Health Check Endpoint

```text
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

### 3. Version Endpoint

```text
GET /version
```

Response:

```json
{
  "version": "1.0.0"
}
```

### 4. Info Endpoint

```text
GET /info
```

Initial response:

```json
{
  "app_name": "Deployment Tracker API",
  "developer": "Oluwatoni Ajaka",
  "role": "Information Technology Student",
  "version": "1.0.0"
}
```

Updated response after redeployment:

```json
{
  "app_name": "Deployment Tracker API",
  "developer": "Oluwatoni Ajaka",
  "position": "Searching intern",
  "role": "Information Technology Student",
  "version": "2.0.0"
}
```

---

## How the Pipeline Works

1. Code is pushed to the `main` branch.
2. GitHub Actions starts the workflow.
3. The app is built into a Docker image.
4. The Docker image is pushed to Amazon ECR.
5. GitHub Actions connects to EC2 over SSH.
6. EC2 pulls the latest image from ECR.
7. The old container is stopped and removed.
8. A new container is started automatically.

---

## Deployment Workflow

The workflow file is stored at:

```text
.github/workflows/deploy.yml
```

It handles:

- checkout
- AWS OIDC authentication
- ECR login
- Docker build
- tag image
- push image
- SSH deployment to EC2

---

## Key Commands Used

### Build Docker image locally

```bash
docker build -t cicd-pipeline-app .
```

### Login to ECR

```bash
aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 533267258346.dkr.ecr.eu-west-1.amazonaws.com
```

### Tag image

```bash
docker tag cicd-pipeline-app:latest 533267258346.dkr.ecr.eu-west-1.amazonaws.com/cicd-pipeline-app:latest
```

### Push image to ECR

```bash
docker push 533267258346.dkr.ecr.eu-west-1.amazonaws.com/cicd-pipeline-app:latest
```

### Pull image on EC2

```bash
docker pull 533267258346.dkr.ecr.eu-west-1.amazonaws.com/cicd-pipeline-app:latest
```

### Run container on EC2

```bash
docker run -d --name cicd-pipeline-app -p 80:5000 --restart unless-stopped 533267258346.dkr.ecr.eu-west-1.amazonaws.com/cicd-pipeline-app:latest
```

---

## Screenshots

## 1. Creating the Amazon ECR Repository

### Search for ECR in AWS Console
![Screenshot 2026-04-16 215836](Screenshot 2026-04-16 215836.png)

### Amazon ECR landing page
![Screenshot 2026-04-16 215858](Screenshot 2026-04-16 215858.png)

### Repository configuration
![Screenshot 2026-04-16 215955](Screenshot 2026-04-16 215955.png)

### Image scanning settings
![Screenshot 2026-04-16 220033](Screenshot 2026-04-16 220033.png)

### Private repository created successfully
![Screenshot 2026-04-16 220629](Screenshot 2026-04-16 220629.png)

---

## 2. EC2 Setup

### EC2 dashboard
![Screenshot 2026-04-16 220727](Screenshot 2026-04-16 220727.png)

### Network settings during instance setup
![Screenshot 2026-04-16 222548](Screenshot 2026-04-16 222548.png)

### Inbound SSH rule
![Screenshot 2026-04-16 222830](Screenshot 2026-04-16 222830.png)

---

## 3. Local Docker and ECR Push Troubleshooting

### Local Docker images
![Screenshot 2026-04-17 113508](Screenshot 2026-04-17 113508.png)

### First successful push to ECR
![Screenshot 2026-04-17 114829](Screenshot 2026-04-17 114829.png)

### Verifying pushed ECR images
![Screenshot 2026-04-17 114933](Screenshot 2026-04-17 114933.png)

### Pull attempt with wrong repository reference
![Screenshot 2026-04-17 130842](Screenshot 2026-04-17 130842.png)

### SSH timeout issue to old EC2 public IP
![Screenshot 2026-04-17 131709](Screenshot 2026-04-17 131709.png)

### Local Docker image verification
![Screenshot 2026-04-17 132010](Screenshot 2026-04-17 132010.png)

---

## 4. Connecting to EC2 and Running the Container

### Initial SSH connection to EC2
![Screenshot 2026-04-17 133755](Screenshot 2026-04-17 133755.png)

### Login to ECR from EC2 and pull image
![Screenshot 2026-04-17 134359](Screenshot 2026-04-17 134359.png)

### Running the container on EC2
![Screenshot 2026-04-17 134452](Screenshot 2026-04-17 134452.png)

### App root endpoint working in browser
![Screenshot 2026-04-17 134559](Screenshot 2026-04-17 134559.png)

### Health endpoint working in browser
![Screenshot 2026-04-17 134630](Screenshot 2026-04-17 134630.png)

### Version endpoint working
![Screenshot 2026-04-17 134743](Screenshot 2026-04-17 134743.png)

### Info endpoint working
![Screenshot 2026-04-17 134800](Screenshot 2026-04-17 134800.png)

---

## 5. IAM OIDC Provider and Role Setup

### GitHub OIDC identity provider
![Screenshot 2026-04-17 141742](Screenshot 2026-04-17 141742.png)

### OIDC provider details
![Screenshot 2026-04-17 141756](Screenshot 2026-04-17 141756.png)

### Creating IAM role with Web identity
![Screenshot 2026-04-17 141813](Screenshot 2026-04-17 141813.png)

### Naming the IAM role
![Screenshot 2026-04-17 142902](Screenshot 2026-04-17 142902.png)

### Trust relationship policy
![Screenshot 2026-04-17 143612](Screenshot 2026-04-17 143612.png)

### Attached permissions policy
![Screenshot 2026-04-17 143624](Screenshot 2026-04-17 143624.png)

---

## 6. GitHub Actions Workflow Setup

### Workflow file in repository
![Screenshot 2026-04-17 144515](Screenshot 2026-04-17 144515.png)

### Editing `deploy.yml`
![Screenshot 2026-04-17 144901](Screenshot 2026-04-17 144901.png)

### GitHub Actions workflow runs
![Screenshot 2026-04-17 145759](Screenshot 2026-04-17 145759.png)

### Updated workflow file for ECR and EC2 deployment
![Screenshot 2026-04-17 150134](Screenshot 2026-04-17 150134.png)

### Workflow running after update
![Screenshot 2026-04-17 150336](Screenshot 2026-04-17 150336.png)

---

## 7. GitHub Actions Deployment Debugging

### Deploy step logs
![Screenshot 2026-04-17 210912](Screenshot 2026-04-17 210912.png)

### EC2 security group showing restricted SSH source
![Screenshot 2026-04-17 211210](Screenshot 2026-04-17 211210.png)

### Successful retry after fixing SSH key
![Screenshot 2026-04-17 211655](Screenshot 2026-04-17 211655.png)

### Info endpoint confirming deployment
![Screenshot 2026-04-17 212327](Screenshot 2026-04-17 212327.png)

---

## 8. Image SHA Tagging and Automatic Redeployment

### SHA-based deployment workflow success
![Screenshot 2026-04-17 213548](Screenshot 2026-04-17 213548.png)

### SHA tagging workflow details
![Screenshot 2026-04-17 213557](Screenshot 2026-04-17 213557.png)

### Multiple GitHub Actions runs showing deployment history
![Screenshot 2026-04-17 214056](Screenshot 2026-04-17 214056.png)

### Updated app info after redeployment
![Screenshot 2026-04-17 214122](Screenshot 2026-04-17 214122.png)

### IAM roles list including deployment roles
![Screenshot 2026-04-17 214500](Screenshot 2026-04-17 214500.png)

---

## AWS Services Used

### Amazon ECR
Used to store Docker images securely.

### Amazon EC2
Used to host and run the Docker container.

### IAM
Used for:
- EC2 permissions
- GitHub Actions OIDC authentication
- secure role assumption

---

## Security Highlights

- GitHub Actions uses **OIDC**
- no permanent AWS access keys are stored in the workflow
- EC2 pulls images securely from private ECR
- SSH deployment is controlled through a GitHub secret and security group rules

---

## Lessons Learned

This project helped me learn how to:

- build a complete CI/CD pipeline from scratch
- use Docker with Flask
- create and manage ECR repositories
- deploy containers to EC2
- configure IAM roles and trust relationships
- use GitHub Actions for automated deployment
- debug common errors involving:
  - Docker
  - ECR
  - IAM
  - SSH keys
  - security groups
  - GitHub Actions workflow failures

---

## Future Improvements

- add Nginx reverse proxy
- attach a custom domain
- add HTTPS with SSL
- improve rollback strategy
- monitor logs with CloudWatch
- clean up workflow warnings
- strengthen production security rules

---

## Author

**Oluwatoni Ajaka**

---

## License

This project is for learning, demonstration, and portfolio purposes.
