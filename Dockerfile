FROM python:3.12.4-bullseye
COPY my_app.py /my_app.py
ENTRYPOINT ["python", "my_app.py"]