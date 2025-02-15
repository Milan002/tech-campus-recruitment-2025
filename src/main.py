import sys
import os

def extract_logs(input_file, target_date):
    # Define the output file path
    output_file = os.path.join("output", f"output_{target_date}.txt")
    try:
        # Check if output directory exists, create it if not
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(input_file, 'r') as file:
            with open(output_file, 'w') as output:
                for line in file:
                    # Check if the line starts with the target date
                    if line.startswith(target_date):
                        output.write(line)

        print(f"Logs for {target_date} have been saved to {output_file}. Please check the output directory.")
    
    except FileNotFoundError:
        print(f"Error: The file name {input_file} does not exist. There was an error extracting logs.")
    except Exception as e:
        print(f"An error occurred: {e} while extracting logs.")

def validate_date_format(date_str):
    """ Validates the date format YYYY-MM-DD """
    if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
        return False
    try:
        year, month, day = map(int, date_str.split('-'))
        # Basic validation for year, month, day range (optional but nice to have)
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return False
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python3 src/main.py YYYY-MM-DD (e.g., python3 src/main.py 2024-11-11)")
        sys.exit(1)

    # Get the target date from the command-line argument
    target_date = sys.argv[1]

    # Validate the date format
    if not validate_date_format(target_date):
        print("Error: Date must be in the format YYYY-MM-DD. (e.g., 2024-11-11)")
        sys.exit(1)

    # Define the input log file (make sure to provide the correct path)
    input_file = "logs_2024.log"

    # Call the function to extract logs
    extract_logs(input_file, target_date)

print("Usage: python3 src/main.py YYYY-MM-DD (e.g., python3 src/main.py 2024-11-11)")