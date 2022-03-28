beforeEach(() => console.log('1 - beforeEach'));
afterEach(() => console.log('1 - afterEach'));

test('', () => console.log('1 - test'));

describe('Scoped / Nested block', () => {
  beforeEach(() => console.log('2 - beforeEach'));
  afterEach(() => console.log('2 - afterEach'));

  test('', () => console.log('2 - test'));
});

// - beforeEach // antes de cada teste
// - test // o teste
// - afterEach // depois de cada teste
// - beforeEach // antes de cada teste
// - beforeEach // antes de cada teste dentro do describe
// - test // o teste dentro do describe
// - afterEach // depois de cada teste dentro do describe
// - afterEach // depois de cada teste