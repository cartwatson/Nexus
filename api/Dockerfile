FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install

COPY . .

CMD ["pip install", "-r", "requirements.txt;"]
CMD ["python", "-u", "api.py;"]
# This commented out ENTRYPOINT will start the container but not
# the python program. I have found this useful for debugging
# ENTRYPOINT ["tail", "-f", "/dev/null"]
