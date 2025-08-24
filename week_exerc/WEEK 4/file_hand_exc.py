def file_read_write():
    try:
        # Ask for file name in user 
        filename = input("Write a file name to read: ")

        # Try to open the file to read 
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        # Simple modification : To convert text to uppercase words
        modified_content = content.lower()

        # Create a new out file 
        new_filename = "modified_" + filename
        with open(new_filename, "w", encoding="utf-8") as f:
            f.write("=== VERSÃO MODIFICADA ===\n\n")
            f.write(modified_content)

        print(f" File '{new_filename}' created with success!")

    except FileNotFoundError:
        print(" Error: The  file doesn't exist.")
    except PermissionError:
        print(" Error: You don't have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


# To perform the function 
file_read_write()