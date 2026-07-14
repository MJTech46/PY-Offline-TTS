import os
import time


GENERATED_FOLDER = ".tmp"

# Delete files older than 2 minutes
DELETE_AFTER = 120

def cleanup_now():

    now = time.time()

    for filename in os.listdir(GENERATED_FOLDER):

        filepath = os.path.join(GENERATED_FOLDER, filename)

        if not os.path.isfile(filepath):
            continue

        age = now - os.path.getmtime(filepath)

        if age > DELETE_AFTER:
            try:
                os.remove(filepath)
                print(f"Deleted: {filename}")
            except Exception as e:
                print(e)