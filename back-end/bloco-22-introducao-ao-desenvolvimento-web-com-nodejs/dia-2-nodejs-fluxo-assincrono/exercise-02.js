const recebe = require('./exercise-01.js');

const result = recebe.recebeParams(1, 2, 3);
console.log(result);



const getRandomNumber = () => { return Math.random() * 100 + 1; }


function main() {
  // console.log(getRandomNumber());
  const result = recebe.recebeParams(
    getRandomNumber(),
    getRandomNumber(),
    getRandomNumber());

  const randomNumbers = Array.from({ length: 3 }).map(getRandomNumber);
  console.log(randomNumbers);

  return randomNumbers;

}

main();
