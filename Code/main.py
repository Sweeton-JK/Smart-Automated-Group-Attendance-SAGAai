# scheduler.py

import schedule
import time
import subprocess

def run_ipynb(notebook_path):
    # Convert IPython notebook to script
    subprocess.run(['../../../Library/Python/3.7/bin/jupyter', 'nbconvert', '--to', 'script', "./faceExtraction.ipynb"])

    # Get the script file name
    script_name = notebook_path.replace('.ipynb', '.py')

    # Run the generated script
    subprocess.run(['python', script_name])

# Schedule the script to run every day at 3:00 AM
schedule.every().day.at("14:31").do(run_ipynb, notebook_path='your_notebook.ipynb')

# Keep the script running to check for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
