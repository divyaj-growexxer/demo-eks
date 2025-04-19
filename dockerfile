
FROM 276445149463.dkr.ecr.us-east-1.amazonaws.com/eks-app-ecr:latest
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
COPY --chown=appuser:appgroup . /app
USER appuser
ENV PORT=8501
EXPOSE $PORT
CMD ["streamlit", "run", "Code.py"]
