FROM python:3.9 alpine
WORKDIR /app/backend
COPY requirements.txt /app/backend
RUN pip install -r requirements.txt
COPY . /app/backend
EXPOSE 8000
CMD python /app/backend/Calculator_syedahmed.py runserver 0.0.0.0:8000
