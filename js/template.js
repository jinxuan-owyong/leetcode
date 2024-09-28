const chunk = require('lodash/chunk');

const method = null
const testSize = 1;
const puzzles = [];

chunk(puzzles, testSize).forEach((args) => {
  const result = method(...args);
  console.log(result);
});
