FROM python:3.12

COPY . /app

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync --no-cache --no-dev

CMD ["uv", "run", "server.py"]
