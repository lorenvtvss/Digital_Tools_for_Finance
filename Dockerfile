# syntax=docker/dockerfile:1
FROM  jupyter/scipy-notebook:python-3.10.8

ENV JUPYTER_ENABLE_LAB=no

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["python", "./notebooks/main.ipynb"]
