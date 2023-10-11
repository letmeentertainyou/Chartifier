'use strict'
/* 
With the exception of intDiv I wrote these and you can copy them into any project you desire.
*/


/* ########## UTIL ##########  */

// Easier for debugging, these are always tmp and need to be removed before committing.
const echo     = message   => document.write(message)
const nl       = _         => document.write('<br>')

// Insanely useful
const deepCopy = iterable  => JSON.parse(JSON.stringify(iterable))

// Populates an array with num to use xfill do this
// array += [...xfill(35, 0)]
const xfill = (copies, num) => Array(copies).fill(num)

//Stolen from random.js, only here for future projects that don't include random.js
//const intDiv = (a, b) => (a - a % b) / b


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
function sum(iterable) {
    var total = 0
    for (let x of iterable) {
        total += x
    }
    return total
}


function arrayComp(iterableA, iterableB) {
    var A = iterableA.toString()
    var B = iterableB.toString()

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

