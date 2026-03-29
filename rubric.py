import re

# Author: Isaac D. Hoyos
# Date: March 29, 2026
def format_rubric(file_path):
    # Notify the user that processing has started.
    print(f"Processing the file '{file_path}' with the unformatted list...")

    # Open the file and clean the lines.
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
                formatted_lines.append("")  # Add a blank line for spacing.

                i += 3
            else:
                break
        else:
            i += 1

    # Overwrite the file with formatted content.
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(formatted_lines))

    # Notify the user that the file has been updated.
    print(f"\nThe file '{file_path}' has been loaded with the new formatted list!")

# Call the function with the target file.
format_rubric("rubric.txt")
