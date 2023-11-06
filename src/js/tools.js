/*
These are a few tools that are not directly related to music theory.
*/

/*
    Deep copy needs to be a builtin for any shallow copy by default languages.
*/
const deepCopy = iterable  => JSON.parse(JSON.stringify(iterable))

/* 
    Populates an array with num to use xfill do this
    array += [...xfill(35, 0)]

    Note that the ellipse is very important.
*/
const xfill = (copies, num) => Array(copies).fill(num)

/*
    Looping through this is wildly inefficient because the loop happens twice.
    So for any large loops just type it out. You can also use this to generate lists 
    of numbers which js doesn't do natively.
*/
function xrange(upper, lower=0, step=1) {
    var result = []
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

/*
    Why this isn't a built in truly eludes me, could computers not add in the 90s?
*/
function sum(iterable) {
    var total = 0
    for (let x of iterable) {
        total += x
    }
    return total
}

/*
    All arrays are unique in js, so we have to convert both arrays into strings, and
    then compare them. This doesn't modify the input arrays.
*/
function arrayComp(iterableA, iterableB) {
    var A = iterableA.toString()
    var B = iterableB.toString()

    if (A == B) {
        return true
    }
    return false
}

/*
    This works like a clock, you change where the start point of the array
    is but not the order of the items in the array, shiftSlice makes music theory
    a lot easier, It's a very useful tool for navigating math in any base.
*/
function shiftSlice(iterable, start) {
    var head = iterable.slice(start, iterable.length)
    var tail = iterable.slice(0, start)
    return  [...head, ...tail]
}

/*
    This one is a bit harder to explain because it's hyper specific to music theory. In music
    theory there is a rule that two notes with the same letter name cannot exist in one key.
    Therefore you cannot have the note Gb in the key of G, you would instead use the note F#.
    This function exists to confirm if a set of seven chords has seven different letter names.
    lenSetFirstChars returns the length of the set of the first chars of an array of strings
    hence the name.
*/
function lenSetFirstChars(listOfStr) {
    var set = new Set()
    for (let i of listOfStr) {
        set.add(i[0])
    }
    var usableSet = Array.from(set)
    return usableSet.length
}
