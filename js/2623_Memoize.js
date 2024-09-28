// 2623. Memoize
/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
  const memo = new Map();
  return function (...args) {
    const key = JSON.stringify(args);
    if (!memo.has(key)) {
      memo.set(key, fn.apply(this, args));
    }
    return memo.get(key);
  };
}

let callCount = 0;
const memoizedFn = memoize(function (a, b) {
  callCount += 1;
  return a + b;
});
memoizedFn(2, 3); // 5
memoizedFn(2, 3); // 5
console.log(callCount); // 1
