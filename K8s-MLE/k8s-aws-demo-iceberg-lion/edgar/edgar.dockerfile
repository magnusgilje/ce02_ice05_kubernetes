FROM python:3.8.12-slim

RUN mkdir build

WORKDIR /build

COPY . .

RUN pip install safety pylint pytest pytest-cov requests bs4 fastapi uvicorn pandas lxml parser-libraries tqdm yahoofinancials fake-useragent



EXPOSE 80

CMD python -m uvicorn main:app --host 0.0.0.0 --port 80