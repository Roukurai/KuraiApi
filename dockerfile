FROM python:3.10.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN groupadd -r al && useradd -r -g al al

WORKDIR /KuraiApi

COPY data/requirements.txt data/requirements.txt
RUN pip install --no-cache-dir -r data/requirements.txt

COPY . .
RUN chown -R al:al /KuraiApi
RUN chmod +x data/setup.sh
RUN ls

EXPOSE 8000
USER al

# CMD [ "uvicorn","main:app","--host", "<host_computer_ip>","--port","8000]
# CMD [ "uvicorn","main:app","--host", "0.0.0.0","--port","8000"]
CMD ["sh", "-c", "data/setup.sh && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]
# CMD [ "uvicorn","main:app"] 