# 🚀 Flask App with CI/CD using GitHub Actions & DockerHub

Welcome to this simple yet powerful project!  
This repository demonstrates how to build, containerize, and deploy a **Flask** web application using **GitHub Actions** for CI/CD and **DockerHub** for image hosting.

---

## 📌 Project Overview

This project starts with creating a **basic Flask app**. It then sets up a **CI/CD pipeline** using GitHub Actions to:

- Automatically build the Docker image.
- Push the image to **DockerHub**.
- Simplify deployment processes.

---

## 🐍 Tech Stack

- Python 3.x
- Flask
- Docker
- GitHub Actions

---

## 💻 Local Setup

1️⃣ **Clone the repository**

```bash
git clone https://github.com/datasign-tist/Project-04-Github-Actions-Using-CICD-Pipeline-Using-Flask-and-DockerHub.git
cd Project-04-Github-Actions-Using-CICD-Pipeline-Using-Flask-and-DockerHub
```

2️⃣ **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the Flask app**

```bash
python app.py
```

Now your app should be running on:

```
http://0.0.0.0:8080/
```

---

## 🐳 Docker Setup

1️⃣ **Build Docker image**

```bash
docker build -t your-dockerhub-username/flask-app .
```

2️⃣ **Run Docker container**

```bash
docker run -p 5000:5000 your-dockerhub-username/flask-app
```

Now visit:

```
http://localhost:5000/
```

---

## 🔁 CI/CD Pipeline

Using **GitHub Actions** to automate:

✅ Code Build  
✅ Docker Image Build  
✅ Docker Image Push to DockerHub  

### Example Workflow

1. Push code to GitHub.
2. GitHub Actions trigger automatically.
3. Docker image is built and pushed to DockerHub.
4. Image ready for deployment.

**Workflow file:** `.github/workflows/docker-build.yml`

---

## 🏆 DockerHub

Your Docker image will be published to:

```
https://hub.docker.com/r/your-dockerhub-username/flask-app
```

---

## 📄 License

This project is licensed under the MIT License — feel free to use and improve it!

---

## 💡 Contribution

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---