FROM python:3.7-alpine
LABEL maintainer='PABLO AZEVEDO <pabloazevedopro@gmail.com>'

WORKDIR /app

ADD requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1 \
    FLASK_ENV=dev \
    TZ=America/Sao_Paulo

ADD ./ /app/

EXPOSE 8000

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8000"]