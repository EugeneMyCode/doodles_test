FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update
RUN apt --fix-broken install
RUN apt-get install google-chrome-stable -y


WORKDIR /doodles_test/
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD python3 -u -m pytest -s --junitxml=result/test-result.xml
