const fs = require('node:fs/promises');
const wordNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
async function main() {
    try {
        const words = await fs.readFile('./input.txt', { encoding: 'utf8' });
        processWords(words);
    } catch(err) {
        console.log(err);
    }

}

function processWords(words) {
    // split string into words
    let arr = words.split('\n');

    let sum = 0;
    let firstNum;
    let secondNum;

    arr.forEach(element => {
        let reverse = element.split("").reverse().join("");
        let firstNumIndex = element.match(/\d/);
        let secondNumIndex = reverse.match(/\d/);
        
        // Checking for strings
        firstNum = evaluateString(element, 'first', firstNumIndex);
        secondNum = evaluateString(element, 'second', secondNumIndex);
        //
        if (firstNum && secondNum) {
            let concatinateNumber = String(firstNum) + String(secondNum);
            sum += Number(concatinateNumber);
        }
    });
    console.log(sum);
}

function convertToNumber(word) {
    switch (String(word)) {
        case 'one':
            return 1;
        case 'two':
            return 2;
        case 'three':
            return 3;
        case 'four':
            return 4;
        case 'five':
            return 5;
        case 'six':
            return 6;
        case 'seven':
            return 7
        case 'eight':
            return 8;
        case 'nine':
            return 9;
        case 'zero':
            return 0;
    }
}

function evaluateString(word, whichNum, numberMatch) {
    //Method will check for the first written number in string and return the number
    let wordIndex;
    if (whichNum === 'first') {
        wordIndex = numberMatch ? numberMatch.index : "";
    } else {
        wordIndex = numberMatch ? (word.length - 1) - numberMatch.index : "";
    }
    let num;

    for(let i=0; i < wordNumbers.length; i++) {
        if(word.match(wordNumbers[i])) {
            let currentWordIndex = word.search(wordNumbers[i]);
            
            switch(whichNum) {
                case 'first':
                    if(currentWordIndex < wordIndex || wordIndex === "") {
                        num = convertToNumber(wordNumbers[i]);
                        wordIndex = currentWordIndex; 
                    } 
                    break;
                case 'second':
                    testMultiple = word.matchAll(wordNumbers[i]);
                    testMultiple = Array.from(testMultiple);

                    // testing if there are multiple words and setting the current index to the last
                    if (testMultiple.length > 1) {
                        currentWordIndex = testMultiple.at(-1).index;
                    }
                    
                    if(currentWordIndex > wordIndex || wordIndex === "") {
                        num = convertToNumber(wordNumbers[i]);
                        wordIndex = currentWordIndex; 
                    }
                    break;
            }
            
        };
    };

    if (num === undefined && numberMatch) {
        num = numberMatch[0];
    }
    return num;
}

main();

// vim: set ts=4 et ;
