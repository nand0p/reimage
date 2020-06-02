FROM python:buster

MAINTAINER "nando" <nando@hex7.com>

ARG DATE
ARG REVISION
ARG GOOGLE_API_KEY
ARG GOOGLE_SEARCH_ID

COPY . .
WORKDIR /app

RUN pip install -r requirements.txt
RUN flask --version

RUN sed -i "s|SEDME|$REVISION -- $DATE|g" index.py
RUN sed -i "s|GOOGLE_API_KEY|$GOOGLE_API_KEY|g" index.py
RUN sed -i "s|GOOGLE_SEARCH_ID|$GOOGLE_SEARCH_ID|g" index.py
RUN cat index.py

ENV FLASK_APP index.py
ENV FLASK_ENV production
ENV FLASK_DEBUG 1

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
