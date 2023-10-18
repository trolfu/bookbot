def count_characters(input_string):
    characters = {}
    lowered_input = input_string.lower()

    for character in lowered_input:
        if character in characters:
            characters[character] += 1
        elif character.isalpha():
            characters[character] = 1

    return characters

with open('books/frankenstein.txt') as f:
    file_contents = f.read()

    word_count = len(file_contents.split())

    character_counts = count_characters(file_contents)
    characters_list = list(character_counts.items())
    characters_list.sort(key=lambda character: character[1], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words were found in the document")
    print("")
    for character in characters_list:
        print(f"The '{character[0]}' character was found {character[1]} times")
    print("")
    print("--- End report ---")