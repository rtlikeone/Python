import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user_input = input("Ente a name: ").upper()
# phonetic_alphabet_list = [phonetic_alphabet[i] for i in user_input]
# print(phonetic_alphabet_list)

while True:
    user_input = input("Ente a name: ").upper()
    try:
        phonetic_alphabet_list = [phonetic_alphabet[i] for i in user_input]
    except KeyError:
        print("Only letters of the alphabet.")
    else:
        print(phonetic_alphabet_list)
        break
