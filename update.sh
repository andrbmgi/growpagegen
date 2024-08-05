#!/bin/bash

# Path to the virtual environment
VENV_PATH="./venv"

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Check if the virtual environment activation was successful
if [ $? -ne 0 ]; then
  echo "Failed to activate the virtual environment."
  exit 1
fi

# Run the gen.py script
python gen.py

# Check if gen.py ran successfully
if [ $? -ne 0 ]; then
  echo "gen.py script failed to run."
  deactivate
  exit 1
fi

# Add changes to git
git add data.json

# Commit the changes
git commit -m "Update data.json with latest data"

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
