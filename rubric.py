import re
import os
import time
import platform
import subprocess

# Author: Isaac D. Hoyos
# Date: April 2, 2026
def open_file(file_path):
    # Open the text file based on the user's operating system.
    try:
        system = platform.system()
        if system == "Windows":
            os.startfile(file_path)
        elif system == "Darwin":  # macOS
            subprocess.call(["open", file_path])
        else:  # Linux
            subprocess.call(["xdg-open", file_path])
    except Exception as e:
        print(f"Could not automatically open the text file: {e}")

def format_rubric(file_path):
    # Step 1: Check if the text file exists.
    if not os.path.exists(file_path):
        time.sleep(1)
        print(f"The text file '{file_path}' does not exist. Creating a new text file...")
        time.sleep(2)
        
        # Create the text file.
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("")

        print(f"\nThe text file '{file_path}' has been created!")
        time.sleep(2)

    else:
        time.sleep(1)
        print(f"The text file '{file_path}' has been found!")
        time.sleep(1)

    # Step 2: Open the text file for the user to review or edit.
    print(f"\nOpening the text file '{file_path}' for you to review or edit...")
    time.sleep(2)
    open_file(file_path)

    # Step 3: Wait for user confirmation.
    input("\nAdd or review your rubric items, save the text file, then press Enter here to continue.")

    # Step 4: Ensure the file is not empty before processing.
    while os.path.getsize(file_path) == 0:
        time.sleep(1)
        print(f"\nThe text file '{file_path}' is still empty.")
        
        # Reopen the text file for the user.
        time.sleep(2)
        open_file(file_path)

        # Wait for user confirmation.
        input("\nPlease add your rubric items, save the text file, then press Enter here to continue.")
    
    time.sleep(2)
    print("\nThe rubric items have been detected!")
    time.sleep(1)

    # Notify the user that processing has started.
    print(f"\nProcessing the text file '{file_path}' with the unformatted list...")
    time.sleep(2)

    # Open the text file and clean the lines.
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    formatted_lines = []
    i = 0

    while i < len(lines):
        # Check if the line starts with a numbered item.
        if re.match(r'^\d+\.', lines[i]):
            title = lines[i]
            
            # Retrieve the next two lines.
            if i + 2 < len(lines):
                line1 = lines[i + 1]
                line2 = lines[i + 2]
                formatted_lines.append(title)
                formatted_lines.append(f"- {line1}")
                formatted_lines.append(f"- {line2}")
                formatted_lines.append("")
                i += 3
            else:
                break
        else:
            i += 1

    # Overwrite the text file with formatted content.
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(formatted_lines))

    # Notify the user that the text file has been updated.
    print(f"\nThe text file '{file_path}' has been formatted successfully!")
    open_file(file_path)

# Call the function.
format_rubric("rubric.txt")
