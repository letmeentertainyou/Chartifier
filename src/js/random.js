/*    
This file comes from:
https://github.com/oittaa/random-browser-js/

and is licensed under MIT here:
https://github.com/oittaa/random-browser-js/blob/main/LICENSE

Copyright (c) 2022 oittaa

*/

const BITS_MAX = 48;
const DEFAULT_ENTROPY = 32;
const RAND_MAX = 0xffff_ffff_ffff;

/**
 * Return the integer quotient of the division of a by b.
 */
const intDiv = (a, b) => (a - (a % b)) / b;

/**
 * Return a randomly-chosen element from a non-empty array.
 */
const choice = (arr) => arr[randomInt(arr.length)];

/**
 * Return an int with k random bits.
 */
function randomBits(k) {
    if (!Number.isInteger(k)) {
        throw new TypeError('"k" must be an integer.');
    }
    if (k < 0) {
        throw new RangeError('"k" must be non-negative.');
    }
    if (k > BITS_MAX) {
        throw new RangeError('"k" must be less than or equal to ' + BITS_MAX);
    }
    // bits / 8 and rounded up
    const numBytes = intDiv(k + 7, 8);
    return intDiv(
        randomBytes(numBytes).reduce((acc, cur) => acc * 256 + cur, 0),
        2 ** (numBytes * 8 - k)
    );
}

/**
 * Generates cryptographically strong pseudorandom data. The size argument
 * is a number indicating the number of bytes to generate.
 */
function randomBytes(size) {
    if (Number.isInteger(size)) {
        return window.crypto.getRandomValues(new Uint8Array(size));
    }
    throw new TypeError("The argument must be an integer.");
}

/**
 * Return a random integer n such that min <= n < max.
 */
function randomInt(min, max) {
    if (typeof max === "undefined") {
        max = min;
        min = 0;
    }
    if (!Number.isSafeInteger(min)) {
        throw new TypeError('"min" is not a safe integer.');
    }
    if (!Number.isSafeInteger(max)) {
        throw new TypeError('"max" is not a safe integer.');
    }
    if (max <= min) {
        throw new RangeError('"max" must be greater than "min".');
    }
    const range = max - min - 1;
    if (range >= RAND_MAX) {
        throw new RangeError(
            '"max - min" must be less than or equal to ' + RAND_MAX
        );
    }
    if (range === 0) {
        return min;
    }
    let x;
    do {
        x = randomBits(range.toString(2).length);
    } while (x > range);
    return x + min;
}
