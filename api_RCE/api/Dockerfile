FROM python:3.11-alpine
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt
COPY ./main.py /code/main.py
RUN mkdir -p /code/media/
RUN chwon -R 101:101 /code/media/
EXPOSE 9000
USER 101:101
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]