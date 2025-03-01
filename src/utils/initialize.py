import os


def ask_file_name():
    # Get all .csv files in the 'data' folder
    data_folder = "src\\data"
    csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

    # Check if there are CSV files available
    if not csv_files:
        print("No CSV files found in the 'data' folder.")
        return None

    # Show a numbered list of files
    print("Select a file to be quizzed on:")
    for i, file in enumerate(csv_files, 1):
        print(f"{i}. {file}")

    # Get user choice
    while True:
        try:
            choice = int(input("Enter the number of the file: "))
            print("You entered: ", choice)
            if 1 <= choice <= len(csv_files):
                return csv_files[choice - 1]  # Return the selected file name
            else:
                print("\n ERROR: Invalid number. Please choose a number from the list.", flush=True)
                print()
        except ValueError:
            print("\n ERROR: Invalid input. Please enter a number.", flush=True)
            print()


# Note: future improvment -> error messages are delayed
