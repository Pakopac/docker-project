FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt .
RUN pip install -r requirements.txt 

EXPOSE 5000

COPY . .

CMD ["gunicorn", "app:app", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:5000"]
