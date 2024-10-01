// 2666. Allow One Function Call
const chunk = require('lodash/chunk');

/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function (fn) {
  let called = false;
  return function (...args) {
    if (called) {
      return;
    }
    called = true;
    return fn.apply(this, args);
  };
};

const method = null;
const testSize = 2;
const puzzles = [
  (a, b, c) => a + b + c,
  [
    [1, 2, 3],
    [2, 3, 6],
  ],
  (a, b, c) => a * b * c,
  [
    [5, 7, 4],
    [2, 3, 6],
    [4, 6, 8],
  ],
];

chunk(puzzles, testSize).forEach((args) => {
  const [fn, argsList] = args;
  const onceFn = once(fn);
  argsList.map((a) => {
    console.log(onceFn(...a));
  });
});
