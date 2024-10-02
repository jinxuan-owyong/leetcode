// 2631. Group By
const chunk = require('lodash/chunk');

/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
  return this.reduce((grouped, el) => {
    const key = fn(el);
    if (!grouped[key]) {
      grouped[key] = new Array();
    }
    grouped[key].push(el);
    return grouped;
  }, {});
};

const testSize = 2;
const puzzles = [
  [{ id: '1' }, { id: '1' }, { id: '2' }],
  function (item) {
    return item.id;
  },
  [
    [1, 2, 3],
    [1, 3, 5],
    [1, 5, 9],
  ],
  function (list) {
    return String(list[0]);
  },
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  function (n) {
    return String(n > 5);
  },
];

chunk(puzzles, testSize).forEach((args) => {
  const [params, fn] = args;
  console.log(params.groupBy(fn));
});
