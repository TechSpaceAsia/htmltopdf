FROM openjdk:11-slim-buster

RUN apt update
RUN apt install -y wkhtmltopdf \
  build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
ENV PYTHON_VERSION=3.10.5
RUN wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz && tar -xf Python-$PYTHON_VERSION.tgz
WORKDIR Python-${PYTHON_VERSION}
RUN ./configure --enable-optimizations && make && make install
RUN apt install -y python3-pip && mkdir /code
WORKDIR /code
COPY requirements.txt main.py ./
RUN pip3 install -r requirements.txt

CMD uvicorn --host=0.0.0.0 main:app
