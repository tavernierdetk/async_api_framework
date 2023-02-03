FROM --platform=linux/amd64 python:3.8.15
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN apt-get -qq update

RUN apt-get install libsndfile1 -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get install ffmpeg -y
RUN apt-get install nano -y
RUN pip freeze > requirements.txt
COPY . /app
EXPOSE 590
CMD ["python","-m","gunicorn", "main:app", "-b", ":5901", "-k", "uvicorn.workers.UvicornWorker", "--reload", "--timeout", "1200"]