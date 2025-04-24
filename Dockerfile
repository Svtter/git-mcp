FROM python:3.12

COPY . /app

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync --no-cache --no-dev

COPY . .

# CMD ["uv", "run", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000

CMD ["uv", "run", "server.py"]
