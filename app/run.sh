#!/bin/bash

# go to the backend directory
cd /backend/

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install flask flask-cors

# Run the backend
python3 app.py

# go back to the frontend directory
cd ../frontend/

# Install dependencies
npm install axios primevue@latest --save primeicons@latest --save autoprefixer

# Run the frontend
npm run serve