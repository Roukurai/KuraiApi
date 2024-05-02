FROM python:3.10.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN groupadd -r al && useradd -r -g al al

WORKDIR /KuraiApi

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# CMD [ "uvicorn","main:app","--host", "<host_computer_ip>","--port","8000]
CMD [ "uvicorn","main:app","--host", "0.0.0.0","--port","8000"]
# CMD [ "uvicorn","main:app"]