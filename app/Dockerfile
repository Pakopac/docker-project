FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt .
RUN pip install -r requirements.txt 
RUN apt update && apt install -y netcat

EXPOSE 5000

COPY . .
COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
