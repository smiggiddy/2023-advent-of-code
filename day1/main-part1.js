const fs = require('node:fs/promises');


async function readData() {
    try {
        const words = await fs.readFile('./input.txt', { encoding: 'utf8' });
        processWords(words);
    } catch(err) {
        console.log(err);
    }

}



readData();
function processWords(words) {
    // split string into words
    let arr = words.split('\n');

    let sum = 0;
    let firstNum 
    let secondNum;
    // console.log(test);
    // console.log(test.split("").reverse().join(""));
    //
    //
    arr.forEach(element => {
        let reverse = element.split("").reverse().join("");
        firstNum = element.match(/\d/);
        secondNum = reverse.match(/\d/);
        if (firstNum || secondNum) {
            let concatinateNumber = firstNum[0] + secondNum[0];
            sum += Number(concatinateNumber);
        }
    });

    console.log(sum);
}


// vim: set ts=4 et ;
