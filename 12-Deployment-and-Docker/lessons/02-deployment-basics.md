# Deployment, Docker, and MLOps Fundamentals

## Deployment concepts
A local script, API, and dashboard have different runtime needs. Deployment makes an application available in a target environment with reproducible dependencies, configuration, monitoring, and rollback procedures.

## Docker
A Docker image packages an application and its runtime dependencies. A container is a running instance of an image. Keep images small, use a suitable base image, pin dependencies where practical, use non-root users, and never bake secrets into images.

## Environment configuration
Use environment variables for deployment-specific settings. Keep `.env` files containing secrets out of Git. Provide a `.env.example` with placeholder variable names, not real credentials.

## CI and observability
Automated checks should run tests and static checks on changes. Monitor availability, latency, errors, resource use, and model/data drift where relevant. Logs should avoid passwords, API keys, and unnecessary personal data.

## MLOps
Track dataset versions, model artifacts, metrics, configuration, and experiment parameters. Define a rollback plan and test model behavior after deployment. A successful container build alone does not prove the application is correct or secure.
