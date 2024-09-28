// 2622. Cache With Time Limit

var TimeLimitedCache = function () {
  this.data = new Map();
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  let isExisting = false;
  if (this.data.has(key)) {
    const [_, timeoutId] = this.data.get(key);
    clearTimeout(timeoutId);
    isExisting = true;
  }
  const deleteKey = function () {
    this.data.delete(key);
  };

  const id = setTimeout(deleteKey.bind(this), duration);
  this.data.set(key, [value, id]);

  return isExisting;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  if (!this.data.has(key)) {
    return -1;
  }
  return this.data.get(key)[0];
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  return this.data.size;
};

const timeLimitedCache = new TimeLimitedCache();
console.log(timeLimitedCache.set(1, 42, 1000)); // false
console.log(timeLimitedCache.get(1)); // 42
console.log(timeLimitedCache.count()); // 1

// const timeLimitedCache = new TimeLimitedCache();
// console.log(timeLimitedCache.set(1, 42, 500)); // false
// setTimeout(function () {
//   console.log(timeLimitedCache.get(1)); // -1
// }, 600);

// const timeLimitedCache = new TimeLimitedCache();
// console.log(timeLimitedCache.set(1, 42, 500)); // false
// console.log(timeLimitedCache.get(1)); // 42
// setTimeout(function () {
//   console.log(timeLimitedCache.set(1, 38, 500)); // true

//   setTimeout(function () {
//     console.log(timeLimitedCache.get(1)); // 38
//   }, 400);

//   setTimeout(function () {
//     console.log(timeLimitedCache.get(1)); // -1
//   }, 600);
// }, 400);
