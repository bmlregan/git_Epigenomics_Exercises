FROM python:3.11-slim

LABEL maintainer="Brianna Malaya Regan" \
      version="0.1" \
      description="Docker image for the seqClass.py sequence classifier"

RUN mkdir /scripts

COPY seqClass.py /scripts/seqClass.py

RUN chmod +x /scripts/seqClass.py

ENV PATH="/scripts:${PATH}"
