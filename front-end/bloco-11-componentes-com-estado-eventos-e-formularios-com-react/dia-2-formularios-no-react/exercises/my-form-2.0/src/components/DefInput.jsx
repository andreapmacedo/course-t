import React from 'react';

class DefInput extends React.Component {
  render() {
    const { value, type, name, onInputChange } = this.props;
    return (
      <label htmlFor="type">
        {name}
        <input
          type={ type }
          name={ name }
          value={ value }
          onChange={ onInputChange }
        />
      </label>);
  }
}

export default DefInput;