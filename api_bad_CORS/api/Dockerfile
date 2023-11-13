FROM python:3.11-alpine
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt
COPY ./main.py /code/main.py
RUN echo "20000" > /code/money.txt
EXPOSE 8080
USER 101:101
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]