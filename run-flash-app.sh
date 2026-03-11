#!/bin/bash

# 0. Activate virtual environment
source brain-venv/bin/activate

# 1. Open the browser in the background after a 2-second delay
(sleep 2 && xdg-open http://127.0.0.1:5000) &

# 2. Start the Flask application
# Note: Using 'flask' instead of 'flash' per standard Flask CLI
flask --app app.py run
