# 🎲 Fun API

A simple and fun REST API built with **FastAPI**.

Fun API started as a learning project and now includes entertaining endpoints along with a beautiful random gradient generator that returns both JSON and an interactive web page.

## ✨ Features

* 🎲 Roll one or multiple dice
* 🪙 Flip one or multiple coins
* 🎨 Generate beautiful named gradients
* 🌐 Interactive HTML gradient page
* 📦 JSON API responses
* 📖 Automatic Swagger documentation

## 🚀 Endpoints

| Method | Endpoint         | Description                    |
| ------ | ---------------- | ------------------------------ |
| GET    | `/`              | Homepage                       |
| GET    | `/roll`          | Roll one die                   |
| GET    | `/roll/{count}`  | Roll multiple dice             |
| GET    | `/flip`          | Flip one coin                  |
| GET    | `/flip/{count}`  | Flip multiple coins            |
| GET    | `/gradient`      | Beautiful random gradient page |
| GET    | `/gradient/json` | Random gradient as JSON        |
| GET    | `/docs`          | Interactive API documentation  |

## 🛠️ Built With

* FastAPI
* Python
* uv
* HTML & CSS

## ▶️ Running Locally

Clone the repository:

```bash
git clone <your-repository-url>
cd fun-api
```

Install dependencies:

```bash
uv sync
```

Start the server:

```bash
uv run fastapi run main.py
```

Open your browser:

* http://127.0.0.1:8000
* http://127.0.0.1:8000/docs

## 📁 Project Goal

This project was created to practice backend development with FastAPI while building fun and interactive APIs. It also demonstrates how to return both JSON responses and dynamically generated HTML pages from the same application.

## 📄 License

This project is open source and available under the MIT License.
