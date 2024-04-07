FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
EXPOSE 8000
ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000" ]