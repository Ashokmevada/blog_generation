FROM python:3.12-slim

WORKDIR /blog_generation

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python" , "app.py"]