# Knight Moves

## Assumptions

Standard 8x8 chessboard, and this simple notation for squares:

![](http://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/SCD_algebraic_notation.svg/242px-SCD_algebraic_notation.svg.png)

Standard rules of movement for the Knight piece as outlined on [Wikipedia](http://en.wikipedia.org/wiki/Knight_(chess)#Movement)

## The Challenge

Write a console application, that when provided with a starting position and
ending position on the command line, responds with:

  1. An array of possible series of moves for a knight to get from start to end square, eg, `[a1-b3-d4, a1-c2-b4, ...]`
  2. An empty array if there is no path within 4 squares
  3. An appropriate error message in case of bad data / format

## Some Rules

- Each square the knight travels should be listed with dashes between.
- There should be no looping paths with the same square repeated again in the same series of moves.
- The paths should be sorted alphabetically.
- Ignore any paths with more than 4 moves.

## Examples

The below examples use a short format of: `start square, end square => result`

```
a1, a1 => bad request as any path will have a1 repeated
a1, h1 => [] (empty as can’t do in move limit)
a1, d4 => [a1-b3-a5-c6-d4, a1-b3-c1-e2-d4, a1-b3-c5-e6-d4, a1-b3-d2-f3-d4, a1-b3-d4, a1-c2-a3-b5-d4, a1-c2-b4-c6-d4, a1-c2-d4, a1-c2-e1-f3-d4, a1-c2-e3-f5-d4]
```

## Submission Guidelines

  - App and tests should be written in Python 3, and should be provided in a way
  that all dependencies are easy to install and the app is easy to run - eg.
  virtualenv instructions, or if you’re adventurous via pip or easy_install
  - It’s recommended you provide a README explaining steps required to install
  dependencies and run your solution
  - Your solution should take the start and end square as command line
  parameters, and print out the resulting array of possible moves, sorted
  alphabetically.
  - Simple neat solutions, with clear naming and tests are prefered.
  - Don’t worry about performance.
  - If you’re unsure of anything or are feeling stuck, please ask.
