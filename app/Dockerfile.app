# Get image from tiangolo (FASTApi)
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install netcat for entrypoint
RUN apt update && apt install -y netcat

# Expose on port 5000
EXPOSE 5000

# Entrypoint for waiting connexion with db before run
COPY . .
COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn app:app -w 3 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:5000" ]