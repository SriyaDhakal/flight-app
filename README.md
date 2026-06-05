# ✈️ Flight Booking API

A REST API for booking flights built with Python and Flask to learn DevOps end-to-end.

## 🌐 Live Demo
https://flight-app-production-1407.up.railway.app/flights

## 🛠️ Tech Stack
- **Backend:** Python, Flask, SQLite
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)
- **CI/CD:** GitHub Actions
- **Deployment:** Railway

## 🏗️ Project Structure
flight_app/
├── main.py              # Flask API entry point
├── models/              # Data models (Flight, Booking, Passenger)
├── services/            # Business logic (flight and booking services)
├── database/            # Database setup and connection
├── kubernetes/          # Kubernetes deployment and service files
├── .github/workflows/   # GitHub Actions CI/CD pipeline
└── Dockerfile           # Container definition
## 🚀 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /flights | Get all flights |
| GET | /flights/<id> | Get flight by ID |
| GET | /flights/search?origin=X&destination=Y | Search flights |
| GET | /bookings | Get all bookings |
| POST | /bookings | Book a ticket |
| DELETE | /bookings/<id> | Cancel a booking |

## ⚙️ How the DevOps Pipeline Works
1. Code pushed to GitHub
2. GitHub Actions automatically builds Docker image
3. Kubernetes manages 2 replicas for high availability
4. If a pod crashes Kubernetes automatically restarts it
5. App is deployed live on Railway

## 🐳 Run with Docker
```bash
docker build -t flight-app .
docker run -p 5000:5000 flight-app
```

## ☸️ Run with Kubernetes
```bash
minikube start
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
minikube service flight-app-service --url
```

## 💡 What I Learned
- Building REST APIs with Flask and SQLite
- Containerizing apps with Docker
- Automating builds with GitHub Actions CI/CD
- Managing containers with Kubernetes (self healing, scaling, replicas)
- Deploying apps to cloud with Railway

## 🎯 Key DevOps Concepts Practiced
- **Docker** — packaging app into a container so it runs the same anywhere
- **CI/CD** — every push to GitHub automatically builds and tests the app
- **Kubernetes** — runs 2 copies of the app, restarts if crashed, scales if needed
- **Cloud Deployment** — live URL accessible by anyone in the world