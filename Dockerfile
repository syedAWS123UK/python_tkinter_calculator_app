FROM python:3.9 -alpine
COPY requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8001
CMD ["python", "syeds_Calculator_.py", "runserver", 0.0.0.0:8001]
