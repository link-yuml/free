#!/bin/bash
cd /workspace/translator
export FLASK_APP=app.py
export FLASK_ENV=development
python app.py