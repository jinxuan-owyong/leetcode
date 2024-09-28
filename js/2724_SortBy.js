// 2724. Sort By
const chunk = require('lodash/chunk');

/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function (arr, fn) {
  arr.sort((a, b) => {
    return fn(a) - fn(b);
  });
  return arr;
};

const method = sortBy;
const testSize = 2;
const puzzles = [
  [5, 4, 1, 2, 3],
  (x) => x,
  [{ x: 1 }, { x: 0 }, { x: -1 }],
  (x) => x.x,
  [
    [3, 4],
    [5, 2],
    [10, 1],
  ],
  (x) => x[1],
];

chunk(puzzles, testSize).forEach((args) => {
  const result = method(...args);
  console.log(result);
});
