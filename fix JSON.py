import json

# Open the existing file for reading
with open('tarot.json', 'r') as file:
    data = json.load(file)

# Print the type and structure of the data to debug
print(type(data))  # Check if data is a list or dictionary

# Modify the structure of the 'interpretation' key
for card_data_list in data.values():  # Iterate over the values (lists) of the dictionary
    for card_data in card_data_list:  # Iterate over each card's data in the list
        print(card_data)  # Print card_data to check its structure
        interpretation = card_data['interpretation']
        card_data['interpretation'] = {
            'normal': interpretation.split('Reversed:')[0].strip(),
            'reversed': interpretation.split('Reversed:')[1].strip() if 'Reversed:' in interpretation else ''
        }

# Write the modified data back to the file
with open('tarot.json', 'w') as file:
    json.dump(data, file, indent=4)
