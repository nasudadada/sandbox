FROM python:3.10

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY .env .

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]
