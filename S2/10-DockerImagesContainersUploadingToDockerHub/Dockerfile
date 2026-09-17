FROM python:3.12-slim

LABEL maintainer="laraibks@gmail.com"

WORKDIR /mlapp

COPY src/predict_rental.py predict_rental.py
COPY requirements.txt requirements.txt
COPY src/data/housing_1000.csv data/housing_1000.csv

# RUN pip install numpy pandas scikit-learn
RUN pip install -r requirements.txt


CMD ["python","predict_rental.py"]
