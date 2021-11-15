FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5000

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY app.py .

CMD ["flask", "run", "--host=0.0.0.0" ]