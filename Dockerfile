FROM python:3.10

RUN useradd --create-home userapi
WORKDIR /films

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ .
RUN chown -R userapi:userapi ./
USER userapi

EXPOSE 5000
CMD ["gunicorn", "-b0.0.0.0:8000", "wsgi:app"]
# CMD ["python", "./wsgi.py"]
