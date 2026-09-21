FROM python:3.14
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./main.py ./main.py
COPY ./app ./app
COPY ./data ./data
CMD ["sh", "-c", "fastapi run main.py --port ${PORT:-80}"]