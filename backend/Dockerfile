FROM python:3.10
RUN apt-get update && apt-get install -y libpq-dev gcc
WORKDIR /app
COPY . /app
RUN pip install --default-timeout=100  -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
