#loading data from json file as adictonary

import json

# Open the JSON file for reading
with open('dictonary.json') as json_file:
    my_dictionary = json.load(json_file)

import difflib

def get_definition(dictionary):
    #.lower()returns all input as lower case
    word = input("Enter a word to get its definition: ").lower()
    if word in dictionary:
        return dictionary[word]
    else:
        closest_match = difflib.get_close_matches(word, dictionary.keys(), n=1)
        if closest_match:
            suggestion = closest_match[0]
            confirmation = input(f"Did you mean '{suggestion}'? Enter 'yes' or 'no': ").lower()
            if confirmation == 'yes':
                return dictionary[suggestion]
            else:
                return "Word not found. Please try again with a different word."
        else:
            return "Word not found. Please try again with a different word."
definition = get_definition(my_dictionary)
print("Definition:", definition)