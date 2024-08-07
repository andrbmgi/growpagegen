#!/bin/bash

git pull
# Check if pull was successful
if [ $? -ne 0 ]; then
  echo "Failed to pull changes from the repository."
  deactivate
  exit 1
fi

# Path to the virtual environment
VENV_PATH="venv"

# Check if the virtual environment directory exists
if [ ! -d "$VENV_PATH" ]; then
  echo "Virtual environment not found at $VENV_PATH"
  exit 1
fi

# Activate the virtual environment
. $VENV_PATH/bin/activate

# Check if the virtual environment activation was successful
if [ $? -ne 0 ]; then
  echo "Failed to activate the virtual environment."
  exit 1
fi

# Run the gen.py script using the virtual environment's Python interpreter
"$VENV_PATH/bin/python" gen.py

# Check if gen.py ran successfully
if [ $? -ne 0 ]; then
  echo "gen.py script failed to run."
  deactivate
  exit 1
fi

# Add changes to git
git add data.json
git commit -m "Update data.json with latest data"

# Download image
"$VENV_PATH/bin/python" image_downloader.py

# Check if image_downloader.py ran successfully
if [ $? -ne 0 ]; then
  echo "image_downloader.py script failed to run."
  deactivate
  exit 1
fi

git add .
git commit -m "Current image"

# Push the changes to the repository
git push

# Check if push was successful
if [ $? -ne 0 ]; then
  echo "Failed to push changes to the repository."
  deactivate
  exit 1
fi

# Deactivate the virtual environment
deactivate

echo "Changes have been successfully pushed to the repository."
