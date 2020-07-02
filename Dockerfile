FROM python:3.6.5
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY fonts /app/fonts
COPY src /app
WORKDIR /app
CMD ["python", "app.py"]
