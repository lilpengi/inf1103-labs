FROM python:3.12-slim

WORKDIR /app

COPY inventory_manager.py .
COPY product.py .
COPY inventory.py .
COPY inventory.json .

CMD ["python", "inventory_manager.py"]