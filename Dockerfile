FROM alpine:3.10
COPY my_app.py /my_app.py
ENTRYPOINT ["python", "my_app.py"]