FROM python:3

RUN pip install flask
RUN mkdir app
WORKDIR /app

ADD app.py .


CMD [ "python", "app.py" ]