import React, { Fragment } from 'react';
import Pokemon from './Pokemon';

class Pokedex extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      pokeIndex: 0,
      selectedPokemons : this.props.pokemons.filter((pokemon) => pokemon.type === 'Fire')
    }
  }

  handleState = (...params) => {
    // console.log(params[0]);
    this.setState({
      pokeIndex: params[0]
    });    
  }

  handleNext = () => {
    if(this.state.pokeIndex < this.state.selectedPokemons.length -1)
      this.handleState(this.state.pokeIndex + 1)
    else
      this.handleState(0)
  }

  render() {
    return (
      <Fragment>
        <div className="pokedex">
            {/* {this.props.pokemons.map(pokemon => <Pokemon key={pokemon.id} pokemon={pokemon} />)} */}
            <Pokemon key={this.state.pokeIndex} pokemon={this.state.selectedPokemons.at(this.state.pokeIndex)} />)
        </div>
        <section>
          <button onClick={this.handleNext}>Next</button>
        </section>
      </Fragment>
    );
  }
}

export default Pokedex;