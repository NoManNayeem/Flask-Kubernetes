
# Flask-Kubernetes Project

This repository demonstrates a fullstack application with a **Flask Backend** and a **React Frontend**, containerized using Docker and deployed using Kubernetes.

Repository URL: [Flask-Kubernetes](https://github.com/NoManNayeem/Flask-Kubernetes.git)

---

## Project Structure

```
kubernetes/
├── flask-deployment.yaml         # Kubernetes Deployment and Service for Flask Backend
├── react-deployment.yaml         # Kubernetes Deployment and Service for React Frontend
flask-backend/
├── app.py                        # Flask backend application
├── requirements.txt              # Python dependencies for Flask
├── Dockerfile                    # Docker configuration for Flask
react-frontend/
├── src/                          # Source code for React frontend
├── public/                       # Public assets for React
├── package.json                  # Node.js dependencies for React
├── Dockerfile                    # Docker configuration for React
docker-compose.yml                # Docker Compose file for local multi-container setup
```

---

## Running the Project Locally

### Flask Backend
1. Navigate to the `flask-backend/` directory:
   ```bash
   cd flask-backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. The backend will be available at `http://127.0.0.1:5000`.

### React Frontend
1. Navigate to the `react-frontend/` directory:
   ```bash
   cd react-frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
4. The frontend will be available at `http://localhost:3000`.

---

## Running with Docker and Docker Compose

1. Ensure Docker and Docker Compose are installed on your system.
2. Build and run the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. The React frontend will be available at `http://localhost:3000` and the Flask backend at `http://localhost:5000`.

---

## Running and Deploying with Kubernetes

### Prerequisites
- Install Kubernetes and `kubectl`.
- A running Kubernetes cluster.

### Steps
1. Push the Docker images to a registry:
   ```bash
   docker tag flask-backend <your-registry>/flask-backend:latest
   docker tag react-frontend <your-registry>/react-frontend:latest
   docker push <your-registry>/flask-backend:latest
   docker push <your-registry>/react-frontend:latest
   ```

2. Apply the Kubernetes configuration files:
   ```bash
   kubectl apply -f kubernetes/flask-deployment.yaml
   kubectl apply -f kubernetes/react-deployment.yaml
   ```

3. Check the status of the pods:
   ```bash
   kubectl get pods
   ```

4. Expose the services externally if needed, using `NodePort` or `LoadBalancer`.

---

## Repository
- Repository URL: [Flask-Kubernetes](https://github.com/NoManNayeem/Flask-Kubernetes.git)

---

Enjoy deploying and scaling your fullstack application with Docker and Kubernetes!
