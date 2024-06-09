FROM python:3.10-slim

WORKDIR /app

RUN pip install streamlit

COPY src/front.py /app/front.py

CMD ["streamlit", "run", "front.py"]