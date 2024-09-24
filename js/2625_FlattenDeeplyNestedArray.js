// 2625. Flatten Deeply Nested Array
/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
  const result = [];
  for (const el of arr) {
    if (Array.isArray(el) && n > 0) {
      result.push(...flat(el, n - 1));
    } else {
      result.push(el);
    }
  }
  return result;
};
