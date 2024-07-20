import os

def get_combined_docs(directory, output_file):
    # Define the delimiter to separate content from different files
    delimiter = "\n\n--- End of Document ---\n\n"
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                # includes .py or requirements.txt files
                if file.endswith('.py') or file == 'requirements.txt':
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            # Write the file name and content to the output file
                            outfile.write(f"File: {file_path}\n")
                            outfile.write(content)
                            outfile.write(delimiter)
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")

# Specify the directory to search and the output file
directory_to_search = f'app'
output_file = f'combined_docs_{directory_to_search}.txt'

# Run the function
get_combined_docs(directory_to_search, output_file)

print("Aggregation complete.")
