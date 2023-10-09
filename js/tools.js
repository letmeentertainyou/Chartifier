'use strict'

/* ########## UTIL ##########  */

//easier for debugging, these are always tmp and need to be removed before committing.
const echo = message => document.write(message)
const nl = _ => document.write('<br>')

//Stolen from random.js, only here for future projects that don't include random.js
//const intDiv = (a, b) => (a - a % b) / b

// THIS IS 100% STOLEN FROM THE INTERNET
function combinations(array, size) {

    function p(t, i) {
        if (t.length === size) {
            result.push(t)
            return
        }
        if (i + 1 > array.length) {
            return
        }
        p(t.concat(array[i]), i + 1)
        p(t, i + 1)
    }

    var result = []
    p([], 0)
    return result
}

// Looping through this is wildly inefficient because the loop happens twice
// So for any slow/large loops just type it out. But you can also use this to
// Generate lists of numbers which js doesn't do natively
function xrange(upper, lower=0, step=1) {
    var result = []
    // I hated duplicating this code but upper and lower need to switch place for easy use
    // In python the user has to know to switch the order of the numbers which feels bad.
    if (step === 1) {
        for (let i=lower; i<upper; i++) {
            result.push(i)
        }
    }
    if (step === -1) {
        for (let i=upper; i>lower; i--) {
            result.push(i)
        }
    }
    return result
}

// Why this isn't a built in truly eludes me.
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
    let stringArray = iterator.map(JSON.stringify)
    let uniqueStringArray = new Set(stringArray)
    let results = Array.from(uniqueStringArray, JSON.parse)
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
    var usableSet = Array.from(set)
    return usableSet.length
}
