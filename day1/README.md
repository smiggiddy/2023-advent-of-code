# Day 1: Number Processing

This script reads data from 'input.txt', processes it, and calculates the sum of concatenated numbers based on specific rules.

## Code Overview

The code is written in Node.js and uses the `fs/promises` module for file operations. There are two functions:

1. **readData():** Reads data from 'input.txt' and calls the `processWords` function.

2. **processWords(words):** Splits the input into lines, processes each line, and calculates the sum of concatenated numbers. It uses string manipulation and regex to extract and evaluate numeric values.

## Main Features

- **Concatenation Rule:** Concatenates two numbers from each line based on specific rules.
  
- **String Evaluation:** Converts written numbers (e.g., 'one', 'two') into numeric values.

- **Sum Calculation:** Calculates the sum of concatenated numbers.

## How to Use

1. Ensure Node.js is installed.
2. Save your input in 'input.txt'.
3. Run the script using `node script.js`.

## Example

For input like:
`one three
five two`

The output would be `60`

This is the sum of (13 + 52) based on the specified rules.

Feel free to explore and modify the code for your specific needs!

