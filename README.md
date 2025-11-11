# My Journey to AI Engineering: Building a Production-Grade MLOps System

![Project Status: In Progress](https://img.shields.io/badge/Status-Phase%201%20In%20Progress-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Welcome to my public journal and portfolio for my journey into the field of AI Engineering. This repository is not just a collection of code; it is a structured, real-time documentation of my process for mastering the principles and tools required to build, deploy, and maintain machine learning systems in production.

My name is **NGUYEN Manh Ha**, and I am a software engineer passionate about building robust, scalable systems. This project is my deliberate effort to apply that passion to the unique challenges of Machine Learning Operations (MLOps).

## 🎯 The Mission: From Model to Product

The central thesis of this project is that a machine learning model is only valuable when it is a reliable, integrated part of a software product. Therefore, the goal is not simply to train a predictive model, but to build a **complete, automated MLOps system** around it.

This repository will contain the end-to-end project for predicting **Telco Customer Churn**, where the focus is on the engineering, automation, and operational aspects of the ML lifecycle.

### Core Objectives:
*   **Automated Training:** Create a pipeline that can be triggered automatically to retrain and validate the model on new data.
*   **Model Versioning & Management:** Use a central registry to track, version, and manage the lifecycle of all trained models.
*   **Reproducible Environments:** Leverage containerization to ensure that the model and its environment are perfectly reproducible.
*   **Robust Deployment:** Deploy the final model as a scalable, high-performance API ready for production use.
*   **Continuous Integration & Delivery:** Implement CI/CD pipelines to automate testing and deployment, bringing DevOps best practices to the ML workflow.

## 🛠️ The Tech Stack: Tools of the Trade

This project is a vehicle for me to gain deep, hands-on expertise with the industry-standard MLOps technology stack.

*   **Core Language:** Python
*   **ML Framework:** Scikit-learn (for its focus on robust, production-ready pipelines)
*   **Experiment Tracking:** MLflow (for logging, model registry, and reproducibility)
*   **Containerization:** Docker (for creating immutable, portable application environments)
*   **API Development:** FastAPI (for high-performance, modern model serving)
*   **CI/CD Automation:** GitHub Actions (for automating the testing and deployment lifecycle)
*   **Workflow Orchestration:** Apache Airflow (for scheduling and managing complex training workflows)
*   **Cloud & IaC:** AWS (S3), Terraform (for managing infrastructure as code)

## 🗺️ The Roadmap: A Phased Approach

My learning and development process is broken down into three distinct phases, each with a clear set of deliverables. This repository will be updated as I progress through this roadmap.

---

### **Phase 1: Foundational MLOps & Production Readiness (In Progress)**
*Goal: To build, containerize, and deploy a single, reliable ML model as a cloud-aware API.*

*   [⏳] **Milestone 1:** Develop a reproducible training pipeline using `Scikit-learn` and track experiments with `MLflow`.
*   [ ] **Milestone 2:** Containerize the entire application with `Docker` to ensure a consistent environment.
*   [ ] **Milestone 3:** Deploy the model as a production-ready REST API using `FastAPI`.
*   [ ] **Milestone 4:** Integrate with cloud storage (AWS S3) to decouple the system from the local filesystem.

---

### **Phase 2: Automation and Scalability (Coming Soon)**
*Goal: To build an automated factory around the model, removing manual steps from the ML lifecycle.*

*   [ ] **Milestone 5:** Automate the entire training and validation process using `Apache Airflow`.
*   [ ] **Milestone 6:** Implement a full CI/CD pipeline with `GitHub Actions` to automatically test code and publish the service container.
*   [ ] **Milestone 7:** Manage all required cloud infrastructure programmatically using `Terraform`.

---

### **Phase 3: Advanced Architectures & Reliability (Coming Soon)**
*Goal: To master the patterns required to run complex AI systems reliably at scale.*

*   [ ] **Milestone 8:** Implement a robust monitoring and alerting system for data drift and model performance.
*   [ ] **Milestone 9:** Explore advanced deployment strategies like Canary Releases on a platform like `Kubernetes`.
*   [ ] **Milestone 10:** Apply these MLOps principles to a more complex Deep Learning model (e.g., in the NLP or CV domain).

## 💬 Let's Connect!

I am building this project in public to share my journey, solidify my knowledge, and connect with others in the field. If you have any questions, suggestions, or just want to connect, please feel free to reach out.

*   **LinkedIn:** https://www.linkedin.com/in/manh-ha-nguyen-401672397/

Thank you for visiting. I look forward to sharing my progress with you.
