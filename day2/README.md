# Day 2: Game Playability Checker

This script analyzes game data from 'input.txt', checks the playability of each game based on cube colors and values.

## Code Overview

The code is written in Node.js and uses the `fs/promises` module for file operations. There are two functions:

1. **readData():** Reads data from 'input.txt' and calls the `processData` function.

2. **processData(file):** Splits the input into lines, processes each game, and checks the playability based on cube colors and values.

## Main Features

- **Game Definition:** Parses the input to define multiple games with their corresponding cube colors and values.

- **Playability Check:** Evaluates whether a game is playable by comparing cube values with predefined thresholds.

## How to Use

1. Ensure Node.js is installed.
2. Save your game data in 'input.txt'.
3. Run the script using `node playabilityChecker.js`.


