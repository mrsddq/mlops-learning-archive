FROM python:3.12-slim

LABEL maintainer="laraibks@gmail.com"

WORKDIR /mlapp

COPY src/predict_rental.py predict_rental.py
COPY data/housing_1000.csv data/housing_1000.csv

RUN pip install --no-cache-dir numpy pandas scikit-learn

CMD ["python", "predict_rental.py"]

 
