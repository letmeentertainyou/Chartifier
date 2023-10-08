'use strict'

/* ########## UTIL ##########  */

//easier for dubuggings
function echo(message) {
    console.log(message);
}

// THIS IS 100% STOLEN FROM THE INTERNET
function combinations(array, size) {

    function p(t, i) {
        if (t.length === size) {
            result.push(t);
            return;
        }
        if (i + 1 > array.length) {
            return;
        }
        p(t.concat(array[i]), i + 1);
        p(t, i + 1);
    }

    var result = [];
    p([], 0);
    return result;
}

// Like python's range but js already has a range keyword.
function xrange(count) {
    var res = []
    for (let i=0; i <count; i++)
        res.push(i)
    return res
}

function sum(iterator) {
    var total = 0
    for (let x of iterator) {
        total += x
    }
    return total
}

// Stole this one in it's entirety too. JS is not fun for data stuff.
// Turns a list of lists into a list of strings, then makes a set of those strings
// Then turns that set back into a list to finally get the unique items from the given array
// This should absolutely be a builtin. I will take it anywhere I need sets.
function removeDupeArrays(iterator) {
    let stringArray = iterator.map(JSON.stringify);
    let uniqueStringArray = new Set(stringArray);
    let results = Array.from(uniqueStringArray, JSON.parse);
    return results
}

function arrayComp(iteratorA, iteratorB) {
    var A = iteratorA.toString()
    var B = iteratorB.toString()

    if (A == B) {
        return true
    }
    return false
}

// This works like a clock, you change where the start point of the array
// is but not the order of the items in the array. It's basically required for music theory
function shiftSlice(iterable, start) {
    var head = iterable.slice(start, iterable.length)
    var tail = iterable.slice(0, start)
    return  [...head, ...tail]
}

function lenSetFirstChars(listOfStr) {
    var set = new Set()
    for (let i of listOfStr) {
        set.add(i[0])
    }
    var usableSet = Array.from(set);
    return usableSet.length
}
