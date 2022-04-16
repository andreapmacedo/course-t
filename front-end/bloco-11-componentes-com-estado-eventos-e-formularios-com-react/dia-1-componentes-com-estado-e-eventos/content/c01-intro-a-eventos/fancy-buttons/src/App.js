// import React from 'react';
// import './App.css';

// /* Embora isso funcione, essa DEFINITIVAMENTE
// não é a maneira correta de se criar eventos
// em React! A função se refere ao componente,
// então deve ser parte de sua classe! */
// function handleClick() {
//   console.log('Clicou no botão!')
// }

// class App extends React.Component {
//   /* Repare que, diferentemente do HTML, no
//   JSX você associa uma função a um evento
//   passando a própria função entre chaves `{}` */
//   render() {
//     return <button onClick={handleClick}>Meu botão</button>
//   }
// }

// export default App;

    // src/App.js
    import React from 'react';

    function handleButtonOne() {
      console.log('Clicou no botão 1!');
    }

    function handleButtonTwo() {
      console.log('Clicou no botão 2!');
    }

    function handleButtonThree() {
      console.log('Clicou no botão 3!');
    }

    class App extends React.Component {
      render() {
        return (
          <div>
            <button onClick={ handleButtonOne }>Botão 1</button>
            <button onClick={ handleButtonTwo }>Botão 2</button>
            <button onClick={ handleButtonThree }>Botão 3</button>
            <button onClick={ handleButtonThree }>Botão 4</button>
          </div>
        );
      }
    }

    export default App;