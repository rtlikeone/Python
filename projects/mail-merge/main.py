# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Get data from .txt file => output into list.
with open("./Input/Names/invited_names.txt") as names:
    # Remove new-lines (\n) with .splitlines()
    names_list = names.read().splitlines()

# for name in names_list:
#     # Open source file in mode="r"
#     with open("./Input/Letters/starting_letter.txt", mode="r") as source:
#         # Open output file in mode="w"
#         with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output:
#             # write to output file with .write()
#             for content in source:
#                 # Replace string with .replace()
#                 content = content.replace("[name]", name)
#                 output.write(content)

with open("./Input/Letters/starting_letter.txt", mode="r") as source:
    source_contents = source.read()
    for name in names_list:
        new_letter = source_contents.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output:
            output.write(new_letter)

