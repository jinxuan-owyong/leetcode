// 2620. Counter
const chunk = require('lodash/chunk');

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function (n) {
  let count = n;
  return function () {
    count += 1;
    return count - 1;
  };
};

const method = createCounter;
const testSize = 2;
const puzzles = [
  10,
  ['call', 'call', 'call'],
  -2,
  ['call', 'call', 'call', 'call', 'call'],
];

chunk(puzzles, testSize).forEach((args) => {
  const counter = createCounter(args[0]);
  args[1].forEach(() => console.log(counter()));
});
