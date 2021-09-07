FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 5000

COPY . .

CMD ["gunicorn", "app:app", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:5000"]
