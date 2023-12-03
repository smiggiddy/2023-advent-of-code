const { warn } = require('node:console');
const fs = require('node:fs/promises');

async function readData() {
    try {
        const inputFile = await fs.readFile('./input.txt', { encoding: 'utf8' });
        processData(inputFile);
    } catch(err) {
        console.log(err);
    }

}

const cubes = {
    'blue': 14,
    'green': 13,
    'red': 12
};

let playableGames = [];

function processData(file){
    let arr = file.split('\n');
    let pattern = /(Game \d.*: )(.*)/
    let gameIDPattern = /(\d.*):/

    const game = (gameID, game) => {
        playAble = [];
        gameArr = game.split(';');


        function  checkPlayable() {
            let max = {'red': 0, 'blue': 0, 'green': 0}
            gameArr.map(item => {
                let splitArr = item.trim().split(',');
                splitArr.filter(index => {
                    let round = index.trim().split(" ");
                    if( max[round[1]] < round[0]) {
                        max[round[1]] = Number(round[0]);
                    }
                });
            });

            return max;
        }

        function printGame() {
            console.log(playAble);
        };
        
        return { printGame, playAble, checkPlayable }

    };
    
    arr.forEach(element => {
        let re = element.match(pattern);
        if (re) {
            let gameID = re[1];
            let currentGame = re[2];
             
            let testGame = game(gameID, currentGame);
            let max = testGame.checkPlayable();
            playableGames.push(max);
            // if (result.length === 0) {
            //     playAble.push(gameID.match(gameIDPattern)[1]);
            //     playableGames.push(gameID.match(gameIDPattern)[1]);
            // }
        };
                 
    });
    // console.log(playableGames);
    let sum = 0;
    playableGames.forEach(item => {
        let power = 1;
        for(key in item) {
            if(item.hasOwnProperty(key)) {
                power *= item[key];
            }
        }
        sum += power;
    });
    console.log(sum);
}

readData();

// vim: set ts=4 et ;
