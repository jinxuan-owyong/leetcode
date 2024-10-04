// 2665. Counter II
const chunk = require('lodash/chunk');

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {
  let count = init;
  return {
    increment: () => {
      count += 1;
      return count;
    },
    decrement: () => {
      count -= 1;
      return count;
    },
    reset: () => {
      count = init;
      return count;
    },
  };
};

const testSize = 2;
const puzzles = [
  5,
  ['increment', 'reset', 'decrement'],
  0,
  ['increment', 'increment', 'decrement', 'reset', 'reset'],
];

chunk(puzzles, testSize).forEach((args) => {
  console.log(args);
  const counter = createCounter(args[0]);
  args[1].forEach((fn) => console.log(counter[fn]()));
});
