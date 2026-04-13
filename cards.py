import re
import os
import sys
import subprocess

# Author: Isaac D. Hoyos
# Date: April 13, 2026

# File path for the cards.txt file.
file_path = "cards.txt"

# Check if the text file exists.
if not os.path.exists(file_path):
    print(f"The {file_path} file was not found. Creating a new text file...")

    # Create an empty text file.
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("")

    print(f"\nA new text file has been created! Please enter your card list, save, and then close the {file_path} file.")

    # Open the text file automatically based on the OS.
    try:
        if sys.platform.startswith('win'):
            os.startfile(file_path) # Windows
        elif sys.platform.startswith('darwin'):
            subprocess.call(['open', file_path]) # macOS
        else:
            subprocess.call(['xdg-open', file_path]) # Linux
    except Exception as e:
        print(f"\nCould not open the text file automatically. Please open the {file_path} file manually.")

    # Stop script so user can edit the text file first.
    input(f"\nPress ENTER after you have added your list and saved the {file_path} file...")

# Template string with placeholders.
template = """🎮 Limited Run Games Series {series} {variant} Trading Card #{card_num} – {name}

✨ Add a rare gem to your collection with this Limited Run Games Series {series} {variant} Trading Card #{card_num} from the {name} Collectible Card Set! A must-have for fans of the {name} franchise and dedicated Limited Run Games collectors.

📌 Item Details:
✅ Authentic Limited Run Games Series {series} Trading Card.
🌟 {variant} Variant – Highly sought after by collectors.
🃏 Card #{card_num} – {name} Set
📊 Condition: Near Mint / Excellent
🛡️ Stored in a protective hard and soft sleeve.
🚭 Smoke-free & pet-free environment.

💎 Why You'll Love It:
Whether you're looking to complete your Limited Run Games trading card collection or searching for a standout piece to display, this card is a perfect addition to any collection. Don't miss out on this trading card because once it's gone, it's gone!

🚚 Shipping & Extras:
📦 FREE Shipping – Fast & Securely Packaged!
📍 Local Pickup Available for Convenience!

💬 Please don't hesitate to contact me with any questions or concerns about this listing! Don't forget to check out my other listings for more amazing collectibles and trading cards!
"""

# Read original text file content.
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

output = []

# Process each line from the text file.
for line in lines:
    line = line.strip()
    
    # Skip empty lines.
    if not line:
        continue
    
    # Regex to extract Series, Variant, Card Number, and Name.
    match = re.match(r"Series (\d+) (\w+) Trading Card #(\d+) (.+)", line)
    
    if match:
        series = match.group(1)
        variant = match.group(2)
        card_num = match.group(3)
        name = match.group(4)
        
        # Fill template with extracted values.
        formatted = template.format(
            series=series,
            variant=variant,
            card_num=card_num,
            name=name
        )
        output.append(formatted)

# Write formatted listings back to the same text file.
with open(file_path, "w", encoding="utf-8") as file:
    file.write("\n\n".join(output))

print(f"\nThe listings have been successfully generated in the {file_path} file!")

# Attempt to open the text file so the user can view the results.
try:
    if sys.platform.startswith('win'):
        os.startfile(file_path) # Windows
    elif sys.platform.startswith('darwin'):
        subprocess.call(['open', file_path]) # macOS
    else:
        subprocess.call(['xdg-open', file_path]) # Linux
except Exception:
    print(f"\nCould not open the text file automatically. Please open the {file_path} file manually.")
