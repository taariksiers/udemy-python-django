FROM python:3.10.4-buster

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY src/ /app

CD /app/simple_social_clone/simplesocial/

EXPOSE 8000

CMD [ "./manage.py", "runserver", "8000" ]
