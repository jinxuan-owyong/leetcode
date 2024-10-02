// 2722. Join Two Arrays by ID
const chunk = require('lodash/chunk');

/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
  const result = {};
  [...arr1, ...arr2].forEach(({ id, ...items }) => {
    result[id] = {
      // spreading result[id] first will allow us to overwrite if already existing
      ...result[id],
      ...items,
    };
  });
  return Object.entries(result)
    .map(([key, value]) => ({ id: +key, ...value }))
    .sort((a, b) => a.id - b.id);
};

const method = join;
const testSize = 2;
const puzzles = [
  [
    { id: 1, x: 1 },
    { id: 2, x: 9 },
  ],
  [{ id: 3, x: 5 }],
  [
    { id: 1, x: 2, y: 3 },
    { id: 2, x: 3, y: 6 },
  ],
  [
    { id: 2, x: 10, y: 20 },
    { id: 3, x: 0, y: 0 },
  ],
  [{ id: 1, b: { b: 94 }, v: [4, 3], y: 48 }],
  [{ id: 1, b: { c: 84 }, v: [1, 3] }],
];

chunk(puzzles, testSize).forEach((args) => {
  const result = method(...args);
  console.log(result);
});
