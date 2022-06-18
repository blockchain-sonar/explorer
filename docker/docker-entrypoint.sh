#!/bin/sh

export PYTHONPATH=/usr/local/blockchain-sonar/backend
source /usr/local/blockchain-sonar/backend/.venv/bin/activate
FLASK_APP=blockchain_sonar_backend \
FLASK_RUN_HOST=0.0.0.0 \
FLASK_RUN_PORT=8080 \
FLASK_ENV=development \
FLASK_DEBUG=0 \
  python -m flask run
