FROM python:3.10.6-alpine
ADD Calculator .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "syeds_calculator.py", "runserver", 0.0.0.0:8000
