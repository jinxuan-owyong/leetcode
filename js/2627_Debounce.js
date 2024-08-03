// 2627. Debounce

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function (fn, t) {
  let timeout;
  return function (...args) {
    if (timeout) {
      clearTimeout(timeout);
      timeout = undefined;
    }
    timeout = setTimeout(() => fn(...args), t);
  };
};

const log = debounce(console.log, 100);
log('Hello'); // cancelled
log('Hello'); // cancelled
log('Hello'); // Logged at t=100ms

// Runtime
// 42
// ms
// Beats
// 99.39%
// Memory
// 49.46
// MB
// Beats
// 26.95%
