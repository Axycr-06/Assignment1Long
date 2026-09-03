# Assignment1Long
CSC120 Long problems

# 1. WordGrid

File Names
Your program should be in a file named word_grid.py. (NOTE: use an underscore, not a dash.)
Expected Behavior
First recall that a grid is a 2d-list (that is, a list of lists) where the length of each inner list is the same length as the outer list. Your program should read two integer values from the input. The first value is the grid size. The second is a random number seed. The program should use the random number seed to initialize the random number generator, create a grid of size grid size × grid size of randomly generated lower-case letters and, finally, print out the grid of letters one row per line.

Specifically, write a program, in a file named word_grid.py, that behaves as follows:

    At the top of your program after the header comment, import the module​ random:

        import random

    Write a function init(), with no argument, that does the following:
        Use the input()​ function (with no argument) to read in the value of grid_size as the first value read in.
        Use the input()​ function (with no argument) to read in the value of seed_value as the second value read in.
        Initialize the random number generator with the value seed_value.

        Note that your code should not prompt the user for input (that is, you should not supply a string to display to the user). Your program will simply read in two numbers and treat the first one as the grid size (which needs to be an integer) and the second one as the seed (which needs to remain a string). Use the following code to initialize the variables grid_size and seed_value, and then intialize the random number generator:

                grid_size = int(input())
                seed_value = input()
                random.seed(seed_value)
        	

        Return grid_size as the return value of the function.

    Write a function make_grid(grid_size) that takes an integer argument grid_size and creates a grid of size grid_size × grid_size whose elements are randomly generated letters. The function returns the grid created.

    Notes:
        each row of the grid is represented as a list of length grid_size; and
        the grid then consists of a list of grid_size such rows.

        For example: the grid

            a	b	c
            d	e	f
            g	h	i

        is represented as the list of lists

            [ [‘a’, ‘b’, ‘c’], [‘d’, ‘e’, ‘f’], [‘g’, ‘h’, ‘i’] ] 

    Write a function print_grid(grid) that takes a list of lists grid as an argument and prints it out one row per line, with a single comma after each letter except for the last one in the row.

    For example, the grid

        [ [‘p’, ‘q’, ‘r’, ‘s’], [‘t’, ‘u’, ‘v’, ‘w’], [‘x’, ‘y’, ‘z’, ‘a’], [‘b’, ‘c’, ‘d’, ‘e’] ] 

    is printed out as

        p,q,r,s
        t,u,v,w
        x,y,z,a
        b,c,d,e

    Note: The indentation in this example is just to improve readability. The output from your print_grid() function should not have any whitespace at the beginning of any line for indentation purposes.
    Write the​ main()​ function to do the following:
        call init(), which returns the grid size;
        call make_grid() ​ with the grid size as an argument; the function returns the grid created
        call print_grid() using the grid returned by make_grid() as its argument; print out the grid.

Programming Requirements
When converting from a random number to a letter, do not use a big ​if-statement. See the number to letter problem for this.
Development Strategy
The representation of a grid of letters as a list of lists has been explained above. The key issue is to generate letters using the random number generator. (The random number generator is initialized with the random number seed by your init() function.)

    You can use the function random.randint( m, n ) to generate a random integer between the values m and n. For example, random.randint(10, 20) ​ will generate a random integer between 10 and 20. Given this, think of how you can call random.randint(...)​ to generate values such that all possible (lower-case) letters, and only those letters, can be generated?

    Once you have the random number returned by random.randint(...), you have to convert it to a letter. Use your solution for the number to letter problem for this.

Comment: You can import from the random library as follows:

    from random import * 

after which you can simply refer to randint(...), i.e., without having to type the prefix random.. 


# 2. WordSearch
Background
Word search is a word game that involves searching for words in a (random) grid of letters. This program simulates the game by searching for words in a grid. The program differs from the physical game in several ways:

    The physical game is usually played with a 4 × 4 grid. Your program will generalize this to any N × N grid (N ≥ 4), where N is determined by the size of the grid provided (see next bullet point).
    The physical game uses a random grid. Your program will read the grid of letters from a file.
    The physical game is timed: players try to find as many words as they can before a timer runs out. Your program will not have this constraint.
    The pyhsical game includes words found on all diagonals. We will simplify the word search by eliminating all but one diagonal search.

Definitions
Given a grid of letters G and a list of words L, a word in G is legal if it meets the following criteria:

    it is at least three letters long;
    it can be formed from letters in G that are adjacent along a row (two cases: going left-to-right or right-to-left), a column (two cases: going top-to-bottom or bottom-to-top), or a diagonal (one case: going upper-left to lower-right); and
    it can be found in the list of words L.

File Names
Your program should be in a file named word_search.py. (NOTE: use an underscore, not a dash.)
Expected Behavior
Write a program, in a file named word_search.py, to do the following:

    Read in, in this order, the name of a word-list file and a grid-of-letters file. Do not prompt the user, that is, do not supply an argument to input(). Simply read in two file names and treat the first as the name of a word-list file and the second as a grid-of-letters file.
    Read the word-list file into a list and the grid-of-letters file into a square grid. You may assume that these files are organized as follows:
        the word-list file contains one word per line;
        the grid-of-letters consists of N lines, each line consisting of N letters separated by whitespace. (Note: The file may be empty.)
    Search this grid for legal words. Matches of words found in the grid against those in the list-of-words should be case-insensitive.
    Collect the legal words found into a list and then print them out as indicated under Output format below.

Examples
The following is an example of the grid of letters file:

        y c o d e j
        h s e y p k
        l p h b w a
        l o b w x z
        w o b a a i
        p l y y c g

In this example (and as your program can figure out after reading the first line), N = 6. For this grid, the words your program should print out are:

    code, cod, ode, lob (horizontal, L-to-R)
    bow, yes, doc (horizontal, R-to-L)
    spool, pool, way (vertical, top-to-bottom)
    loop, loops (vertical, bottom-to-top)
    lob, wag (diagonal, top-left to bottom-right)

Input files
You can use the file WORDS, which is a list of about 45,000 words, to test your program. However, note that we may also use other word-lists, which may be bigger or smaller than this list, when testing your code. You should test your code using your own word-lists, which can be bigger or smaller than this list and whose words that may or may not be real English words.
Output format
The words you find should be printed in alphabetical order, one to a line without any extra whitespace.

Note: If the grid-of-letters file is empty, there is no output.
Development Strategy
Data Structures
Organize the list of valid words as a list of strings. Organize the grid as a list of lists.
Program development

    Searching horizontally. First, consider the problem of finding words horizontally in the grid going from left to right. Consider the first row in the example shown above:

        y c o d e j 

    Notice that this row contains the words cod, code, and ode. Suppose that the row is represented as the list [‘y’, ‘c’, ‘o’, ‘d’, ‘e’, ‘j’]. A simple way to explore all the possible words (going L to R) in this list would be as follows (the process for the other rows is similar).
        Starting at the first element (i.e., ‘y’), check whether the sequence of length 3 starting at that position is a legal word (we start with length 3 because a legal word has to be at least three letters long). Then check for length 4, then for length 5, etc., until you reach the end of the list.
        Now repeat this step, but starting at the second element (i.e., ‘c’). Notice that this time you will come to the end of the list one step sooner. Then repeat for the third element, and so on.
        In each of these steps, your code is checking a sequence of list elements (e.g., the sequence of elements ‘c’, ‘o’, ‘d’, ‘e’) to see whether this is a word that occurs in your list of words. How can you use the function concat_list() from the Short Problems for this assignment?

    Next consider the problem of searching for words horizontally going right to left. Suppose we want to search the row ​ y c o d e j​ going right to left. This is actually the same as reversing the row, to

        j e d o c y 

    and then searching left to right (a problem you’ve solved already). The key thing to note here is that you’ve taken the problem of searching R-to-L and converted it into an equivalent problem involving an L-to-R search, for which you’ve already written code.
    Searching vertically. Next consider the problem of searching for words vertically, i.e., among columns. Can you use the function column2list() from the Short Problems for this assignment to solve this problem going from top to bottom? Can you figure out a way of using column2list() with list-reversing to solve the problem of searching vertically going from bottom to top?
    Searching diagonally. Searching diagonally is the hardest part of this problem, however, we are only considering one case: upper-left to lower-right.

        If you can extract each diagonal into a list of letters, then you can simply search through this list as you did before—again, reducing this problem to one you’ve already written code to solve.

            Suppose you start the diagonal at position 0 of row 0, i.e., at grid[0][0]. The diagonal elements are y s h f a g and correspond to the index values: [0][0], [1][1], [2][2], ... How do the x- and y-coordinates change as you go from one element to the next? Why do they change in this way?
            Suppose you start the diagonal at position 1 in row 0, i.e., grid[0][1]. The diagonal elements are c e b x i (Note: this diagonal is shorter than the previous one) and correspond to the index values: [0][1], [1][2], [2][3], .... How do the x- and y-coordinates change as you go from one element to the next? Why do they change in this way?
            Repeat this exercise for the diagonal starting at grid[1][0]. Look at how the x- and y-coordinates change from each element to the next. How does this compare to the way they changed for the other two diagonals you considered (above)?

        Do you see a pattern in how the x- and y-coordinates change between successive elements? Can you use this pattern to extract a diagonal going from the upper-left to lower-right given its starting coordinates into a list?

Program Structure
There are many ways to structure a given program, but at the very least, your program is required to have a main() function that calls the functions that you have written to satisfy the Expected Behavior described previously. Specifically, your program should call functions to read the word-list file and the grid of letters file, call one or more functions that find the legal words in the grid, and, finally, call a function to print out the resulting words found.

The use of a main() function and supporting functions described above is similar to the structure that was provided to you for the word_grid.py program.

Note: You may not use global variables.

If you would like more guidance on how to structure your program, you may use the outline below:

    def get_word_list():
        ....
        return a list of valid words 

    def read_letters_files():
        ...
        return a grid of letters
    ...
    more functions are defined here
    ...

    def main():
        word_list = get_word_list()
        letters_grid = read_letters_file() 

        # a list used to accumulate the valid words found
        all_words = []  

        call a function that finds the words appearing horizontally, passing in the needed arguments

        call a function that finds the words appearing vertically, passing in the needed arguments

        call a function that finds words appearing on the diagonals, passing in the needed arguments

        call a function that prints the words found, passing in the needed argument(s)

     main()  

Be sure to follow the style guidelines for commenting your program. 