"""
    File: word_search.py
    Author: Shane Dyke
    Course: CSC 120, Fall 2026
    Purpose: This program processes a word list and a grid of letters 
	to find all valid words hidden within the grid.
"""

def get_word_list():
    fileName = input("")
    with open("fileName", "r") as f:
        return [line.strip() for line in f]

def read_letters_file():
    fileName = input("")
    with open("fileName", "r") as f:
        return [list(line.strip()) for line in f]


def find_words_in_line(line, valid_words):

    line = "".join(line) #line is a list so it turns it into a string

    for word in valid_words:
        if word in line:
            yield word #returns the found word
	


def find_horizontal_words(grid, valid_words):
	
	#L-R
    for row in grid:
        yield from find_words_in_line(row, valid_words)

    #R-L
    for row in grid:
        yield from find_words_in_line(row[::-1], valid_words) #[::-1] flips the row


def find_vertical_words(grid, valid_words):
    """Find words down columns in both directions."""
    # T-B
    for col in range(len(grid[0])):
        column = [grid[row][col] for row in range(len(grid))]
        yield from find_words_in_line(column, valid_words)

    # B-T
    for col in range(len(grid[0])):
        column = [grid[row][col] for row in range(len(grid)-1, -1, -1)]
        yield from find_words_in_line(column, valid_words)


def find_diagonal_words(grid, valid_words):
	"""Find words along upper-left to lower-right diagonals."""
	pass


def print_words(words):
	"""Print the found words in alphabetical order, one per line."""
	pass


def main():
	"""Read input files, search the grid, and print the results."""

    
	word_list = get_word_list()
	letters_grid = read_letters_file()

	all_words = []
	all_words.extend(find_horizontal_words(letters_grid, word_list))
	all_words.extend(find_vertical_words(letters_grid, word_list))
	#all_words.extend(find_diagonal_words(letters_grid, word_list))

	print_words(all_words)


if __name__ == "__main__":
	main()
