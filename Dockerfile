FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install uv
RUN uv sync --frozen

CMD ["uv", "run", "fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]