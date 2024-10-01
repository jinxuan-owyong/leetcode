// 2677. Chunk Array
const chunk2 = require('lodash/chunk');

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function (arr, size) {
  let result = [];
  let i = 0;
  while (i < arr.length) {
    result.push(arr.slice(i, i + size));
    i += size;
  }
  return result;
};

const method = chunk;
const testSize = 2;
const puzzles = [
  [1, 2, 3, 4, 5],
  1,
  [1, 9, 6, 3, 2],
  3,
  [8, 5, 3, 2, 6],
  6,
  [],
  1,
];

chunk2(puzzles, testSize).forEach((args) => {
  const result = method(...args);
  console.log(result);
});
