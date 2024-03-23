import os
from typing import Dict, List

import fire

path_to_words = "/Users/tesslinden/Dropbox/Code/hardback/words.txt" 

def get_words(path_to_words: str) -> List[str]:
    with open(path_to_words) as f:
        words = f.read().splitlines()
    return words


def hardbackCLI(
    lettercounts: Dict[str, int] = None,
    minlength: int = None,
    maxlength: int = None,
    output: str = None,
    printwords: bool = True,
):
    """ 
    Sample usage:

    python hardback.py --lettercounts "{'c': 1, 'w': 1, 's': 2}" --minlength 11 --maxlength 12

    This will print all words found in words.txt with at least 1 'c', 1 'w', 1 'n', and 2 's', 
    with a minimum length of 11 letters and a maximum length of 12 letters.

    Optional arguments:

    --output: str = None
        Path to output file. If output is None, no output file is written.

    --printwords: bool = True
        Whether to print the matching words.

    """

    arguments = [lettercounts, minlength, maxlength]
    assert any(arguments), "Please provide at least one of the following: lettercounts, minlength, maxlength"

    words = get_words(path_to_words)

    # drop words with uppercase or non-alphabetical characters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    words = [word for word in words if all(letter in alphabet for letter in word)]

    # filter for letter counts
    if lettercounts:

        lettercounts = {k.lower(): v for k, v in lettercounts.items()}

        assert (len(set(lettercounts.keys())) == len(lettercounts.keys())), "lettercounts contains duplicate keys"
        assert all([key in alphabet for key in lettercounts.keys()]), "lettercounts.keys() contains invalid characters"
        assert all([type(value) == int for value in lettercounts.values()]), "lettercounts contains non-integer values"
        assert all([value >= 0 for value in lettercounts.values()]), "lettercounts contains negative values"

        words = [word for word in words if all(word.count(letter) >= count for letter, count in lettercounts.items())]

    # filter for min length
    if minlength:
        words = [word for word in words if len(word) >= minlength]

    # filter for max length
    if maxlength:
        words = [word for word in words if len(word) <= maxlength]

    if printwords:
        print(f"\nFound {len(words)} words:\n")
        for word in words:
            print(word)   
    
    if output:
        print(f"\nWriting {len(words)} words to file {output}...")
        write_confirmed = True
        if os.path.exists(output):
            response = ''
            while response not in ['y', 'n']:
                response = input("File already exists. Overwrite? [y/n] ")
            if response == 'n':
                print("Did not write to file.")
                write_confirmed = False
        if write_confirmed:   
            with open(output, 'w') as f:
                for word in words:
                    f.write(word + '\n')
            print("Done.")
    
    print()
    return

if __name__ == "__main__":
    fire.Fire(hardbackCLI)
