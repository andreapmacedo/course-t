const math = require('./exercise-01.js');

const result = math.doMath(1, 2, 3);
console.log(result);



const getRandomNumber = () => { return Math.random() * 100 + 1; }


function callDoMath() {
  
  // forma 1
  const result = math.doMath(
    getRandomNumber(),
    getRandomNumber(),
    getRandomNumber());

  // forma 2
  const randomNumbers = Array.from({ length: 3 }).map(getRandomNumber);
  console.log(randomNumbers);

  return randomNumbers;

}

// Não funciona
// math.mathParams(...callDoMath)
//   .then((result) => console.log(result))
//   .catch((err) => console.error(err.message));

callDoMath();
