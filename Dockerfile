FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY SimpleCalculator/calculator/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY SimpleCalculator ./SimpleCalculator

WORKDIR /app/SimpleCalculator

ENTRYPOINT ["python", "main.py"]
CMD ["--help"]
