# hardback-hacker

## Description

For when you can't hack it at the game [Hardback](https://boardgamegeek.com/boardgame/223750/hardback).

## Usage

`$ python hardback.py --lettercounts "{'c': 1, 'w': 1, 's': 2}" --minlength 11 --maxlength 12`

This will print all English words with at least 1 'c', 1 'w', 1 'n', and 2 's', with a minimum 
length of 11 letters and a maximum length of 12 letters.

Optional arguments:

`--output: Optional[str] = None` 
    Path to output file. if output is None, no output file is written.

`--printwords: bool = True` 
    Whether to print the matching words.

## Note
The words.txt file provided here was obtained in january 2024 from https://github.com/dwyl/english-words/blob/master/words.txt
