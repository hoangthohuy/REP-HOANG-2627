FROM python:3.14-slim@sha256:cfe2e24a75302a15934d37c2d86412893c0aa934dc3a97cbb439d04c01890ca9

WORKDIR /app

COPY . /app

# RUN pip install -r requirements.txt

CMD ["sh", "-c", "python banquier.py & python distributivity.py & wait"]

