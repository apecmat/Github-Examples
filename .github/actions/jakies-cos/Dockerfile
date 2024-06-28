FROM python:3.12.4-bullseye
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyyaml
COPY my_app.py /my_app.py
ENTRYPOINT ["python", "/my_app.py"]