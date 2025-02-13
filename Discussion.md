Plan Input and Output: We will receive a date in the format YYYY-MM-DD as an argument. The output will be saved to a file in the format output/output_YYYY-MM-DD.txt.

Efficient Processing: Given the file's size (1 TB), read it line by line to minimize memory usage.

Date Filtering: Logs are in the format YYYY-MM-DD HH:MM:SS LOG_LEVEL Message. We check if each line starts with the target date.

Approach:
• Line-by-line processing to handle large files without high memory consumption.
• Date matching to selectively write matched logs to the output file.
• Error handling for missing or invalid files.

Explanation of the Code:
• Input handling via command-line argument.
• Directory creation for output if needed.
• Writing matched lines to the output file.
• Validating date format before processing.

You can run the code with:
python3 src/main.py 2024-12-01
