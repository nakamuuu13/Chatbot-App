FROM python:3.11.4

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app/src

CMD ["sh", "-c", "python main.py > /app/logs/app.log 2>&1 & tail -f /app/logs/app.log"]