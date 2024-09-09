#!/bin/bash
CONFIG_FILE="data/.config"
TEMPLATE_FILE="data/template.config"

# If the configuration file doesn't exist, create it from the template
if [ ! -f "$CONFIG_FILE" ]
then
  cp "$TEMPLATE_FILE" "$CONFIG_FILE"
  echo "First time setup required. Please edit 'data/.config' to configure the application."
  exit 1  # Exit with an error code to prevent further execution
fi

# Start the application using uvicorn
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
