# AutoPilotOps 

AutoPilotOps is a self-healing backend monitoring platform that automatically
detects, analyzes, and recovers failing APIs with minimal human intervention.

## Problem Statement
Modern backend systems often fail silently. Engineers react only after users
complain. AutoPilotOps proactively detects issues and applies recovery actions.

## What This Project Demonstrates
- API health monitoring
- Failure detection using thresholds
- Log-based root cause analysis
- Automated remediation (simulated)
- System observability via dashboard

## Tech Stack
- Python
- FastAPI
- Django
- Celery & Redis
- React
- Docker

## Architecture
Microservice-based design separating monitoring, analysis, healing,
and visualization responsibilities.

## Project Status
Active development (Day 1 completed)