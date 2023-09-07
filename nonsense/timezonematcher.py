import openpyxl
import re

def extract_and_write_timezones(input_excel_file, sheet_name, output_text_file):
    # Load the Excel workbook
    try:
        workbook = openpyxl.load_workbook(input_excel_file)
    except FileNotFoundError:
        return "Excel file not found."

    # Select the worksheet where your data is located
    try:
        worksheet = workbook[sheet_name]
    except KeyError:
        return f"Worksheet '{sheet_name}' not found."

    # Define your state acronym to timezone dictionary
    state_timezone_dict = {
        'NY': 'Eastern Time',
        'NC': 'Eastern Time',
        # Add more state acronyms and their respective timezones here
    }

    # Create or open a file in append mode for writing the timezones
    with open(output_text_file, 'a') as output_file:
        for row in worksheet.iter_rows(min_col=1, max_col=1, min_row=2):  # Adjust the row range as needed
            full_address = row[0].value

            # Use a regular expression to find state acronyms in the full address
            matches = re.findall(r'\b[A-Z]{2}\b', full_address)

            # Write the matching acronyms to the output file
            for match in matches:
                if match in state_timezone_dict:
                    output_file.write(f'{state_timezone_dict[match]}\n')

    return "Timezones extracted and written successfully."

# Usage example:
result = extract_and_write_timezones('your_excel_file.xlsx', 'Sheet1', 'timezones.txt')
print(result)
