
FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD ["python", "inventory_manager.py"]
