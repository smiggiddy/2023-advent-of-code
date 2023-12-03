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
            let result = gameArr.map(item => {
                let splitArr = item.trim().split(',');
                let playable = splitArr.filter(index => {
                    let round = index.trim().split(" ");
                    return cubes[round[1]] < round[0];

                });

                return playable;
            });

            result = result.filter(item => item.length > 0 );
            return result;
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
            let result = testGame.checkPlayable();
            if (result.length === 0) {
                playAble.push(gameID.match(gameIDPattern)[1]);
                playableGames.push(gameID.match(gameIDPattern)[1]);
            }
        };
                 
    });
    // console.log(playableGames);
    let sum = playableGames.reduce((sum, current) => Number(sum) + Number(current), 0);
    console.log(sum);
}

readData();

// vim: set ts=4 et ;
