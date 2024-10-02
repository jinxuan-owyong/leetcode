// 2704. To Be Or Not To Be
const chunk = require('lodash/chunk');

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function (val) {
  return {
    toBe: (x) => {
      if (x === val) {
        return true;
      }
      throw new Error('Not Equal');
    },
    notToBe: (x) => {
      if (x !== val) {
        return true;
      }
      throw new Error('Equal');
    },
  };
};

const testSize = 1;
const puzzles = [
  () => expect(5).toBe(5),
  () => expect(5).toBe(null),
  () => expect(5).notToBe(null),
];

chunk(puzzles, testSize).forEach(([fn]) => {
  console.log(fn());
});
