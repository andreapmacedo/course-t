// - Caso algum dos parâmetros recebidos não seja um número, rejeite a Promise com o motivo `"Informe apenas números"`.
// - Caso todos os parâmetros sejam numéricos, some os dois primeiros e multiplique o resultado pelo terceiro (`(a + b) * c`).
// - Caso o resultado seja menor que 50, rejeite a Promise com o motivo `"Valor muito baixo"`
// - Caso o resultado seja maior que 50, resolva a Promise com o valor obtido.

const doMath = (a, b, c) => {
  if (typeof a !== "number" || typeof b !== "number" || typeof c !== "number") {
    // throw new Error("Parâmetros inválidos");
    return reject(new Error('Informe apenas números')); // Promise
  }
}

function callDoMath() {
  const params = doMath(1, 2, 3);
  console.log(params);
}

// callDoMath();

module.exports = { doMath };