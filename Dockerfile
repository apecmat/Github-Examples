FROM python:3.12-slim
COPY my_app.py /my_app.py
ENTRYPOINT ["python", "my_app.py"]