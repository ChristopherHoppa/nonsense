# Define the file path
file_path = "your_log_file.log"

# Define the pattern or keyword to look for
pattern = "UNABLE TO INSERT"  # Replace with your specific pattern or keyword

# Define the number of lines to capture before and after the target line
context_lines = 4  # Adjust as needed

# Initialize variables to keep track of context
context_buffer = []

# Open the log file for reading
with open(file_path, "r") as file:
    for line in file:
        # Add the current line to the context buffer
        context_buffer.append(line.strip())

        # Maintain the context buffer size
        if len(context_buffer) > context_lines:
            context_buffer.pop(0)

        # Check if the line contains the pattern or keyword
        if pattern in line:
            # Print the surrounding context lines
            print("Context Lines:")
            for context_line in context_buffer:
                print(context_line)

# Close the file
file.close()
