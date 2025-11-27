FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y build-essential && pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY chroma_db_fons /app/chroma_db_fons
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
