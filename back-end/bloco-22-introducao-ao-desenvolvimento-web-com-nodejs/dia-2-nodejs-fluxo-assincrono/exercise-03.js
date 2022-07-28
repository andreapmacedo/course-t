const math = require('./exercise-01.js');

const getRandomNumber = () => { return Math.random() * 100 + 1; }

async function callDoMath() {

  const randomNumbers = Array.from({ length: 3 }).map(getRandomNumber);
  console.log(randomNumbers);
  const result = await math.doMath(...randomNumbers);
  console.log(result);

  // não funciona
  // math.doMath(...randomNumbers)
  //   .then((result) => console.log(result))
  //   .catch((err) => console.error(err.message));

  try {
    const resultTryCatch = await math.doMath(...randomNumbers);
    console.log(resultTryCatch);
  } catch (err) {
    console.error(err.message);
  }


  return result;

}

callDoMath();