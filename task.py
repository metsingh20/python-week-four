import os

def modify_content(content):
    """
    Convert the text to uppercase.
    """
    return content.upper()

def safe_filename(name):
    """
    Ensures the filename is valid and adds .txt if missing.
    """
    invalid_chars = set(r'<>:"/\|?*')
    if any(c in invalid_chars for c in name):
        return None
    if not name.endswith('.txt'):
        name += '.txt'
    return name

def read_file():
    try:
        raw_name = input("Enter the name of the file to read and modify: ").strip()
        input_filename = safe_filename(raw_name)
        if not input_filename:
            print(" Invalid filename.")
            return
        if not os.path.isfile(input_filename):
            print(" File does not exist.")
            return

        with open(input_filename, 'r') as infile:
            content = infile.read()
            print(f"\nOriginal content from '{input_filename}':\n")
            print(content)

        modified_content = modify_content(content)

        with open(input_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"\n Modified content has been saved (overwritten) in '{input_filename}'.")
    except PermissionError:
        print(" Error: You don't have permission to access this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

def write_file():
    try:
        raw_name = input("Enter the name of the file to write to: ").strip()
        output_filename = safe_filename(raw_name)
        if not output_filename:
            print(" Invalid filename.")
            return

        print("Start typing your content. Type 'SAVE' on a new line when you're done:\n")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'SAVE':
                break
            lines.append(line)

        with open(output_filename, 'w') as outfile:
            outfile.write('\n'.join(lines))

        print(f"\n Your content has been saved to '{output_filename}'.")
    except PermissionError:
        print(" Error: You don't have permission to write to this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

def main():
    print("Do you want to (R)ead and modify or (W)rite a file?")
    choice = input("Enter R or W: ").strip().upper()

    if choice == 'R':
        read_file()
    elif choice == 'W':
        write_file()
    else:
        print(" Invalid choice. Please enter R or W.")

if __name__ == "__main__":
    main()
