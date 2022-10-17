# syntax=docker/dockerfile:1
FROM python:3.9 

COPY . .

RUN pip install pandas numpy matplotlib

# COPY requirements.txt .
# RUN pip install -r requirements.txt

CMD ["python", "./plotdata.py"]