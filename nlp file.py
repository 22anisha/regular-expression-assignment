import re

def extract_nepali_phone_numbers(file_path):
    # Regular expression to match Nepali mobile and landline phone numbers
    phone_pattern = re.compile(r'\b(?:98\d{8}|97\d{8}|96\d{8}|[0-9]{3}-\d{7}|01\d{7}|[0-9]{3}-\d{7})\b')
    
    
    phone_numbers = []
    
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Find all matching phone numbers in the current line
            matches = phone_pattern.findall(line)
            phone_numbers.extend(matches)
    
    return phone_numbers


if __name__ == "__main__":
    # Update with the correct path to your text file
    file_path = 'C:/Users/DELL/Desktop/nlp/sample.txt'  # Use full path or relative path
    phone_numbers = extract_nepali_phone_numbers(file_path)
    
    # Display the extracted phone numbers
    if phone_numbers:
        print("Valid Nepali Phone Numbers:")
        for number in phone_numbers:
            print(number)
    else:
        print("No valid Nepali phone numbers found.")