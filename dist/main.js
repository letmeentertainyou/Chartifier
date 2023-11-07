const BITS_MAX = 48
const DEFAULT_ENTROPY = 32
const RAND_MAX = 0xFFFF_FFFF_FFFF
const intDiv = (a, b) => (a - a % b) / b
const choice = arr => arr[randomInt(arr.length)]
function randomBits (k) {
    if (!Number.isInteger(k)) {
        throw new TypeError('"k" must be an integer.')
    }
    if (k < 0) {
        throw new RangeError('"k" must be non-negative.')
    }
    if (k > BITS_MAX) {
        throw new RangeError('"k" must be less than or equal to ' + BITS_MAX)
    }
    const numBytes = intDiv(k + 7, 8)
    return intDiv(
        randomBytes(numBytes).reduce((acc, cur) => acc * 256 + cur, 0),
        2 ** (numBytes * 8 - k))
}
function randomBytes (size) {
    if (Number.isInteger(size)) {
        return window.crypto.getRandomValues(new Uint8Array(size))
    }
    throw new TypeError('The argument must be an integer.')
}
function randomInt (min, max) {
    if (typeof max === 'undefined') {
        max = min
        min = 0
    }
    if (!Number.isSafeInteger(min)) {
        throw new TypeError('"min" is not a safe integer.')
    }
    if (!Number.isSafeInteger(max)) {
        throw new TypeError('"max" is not a safe integer.')
    }
    if (max <= min) {
        throw new RangeError('"max" must be greater than "min".')
    }
    const range = max - min - 1
    if (range >= RAND_MAX) {
        throw new RangeError('"max - min" must be less than or equal to ' + RAND_MAX)
    }
    if (range === 0) {
        return min
    }
    let x
    do {
        x = randomBits(range.toString(2).length)
    } while (x > range)
    return x + min
}
const deepCopy = iterable  => JSON.parse(JSON.stringify(iterable))
const xfill = (copies, num) => Array(copies).fill(num)
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
var diatonic_notes = { 'C♯': 'D♭', 'F♯': 'G♭', 'B': 'C♭', 'D♭': 'C♯', 'G♭': 'F♯', 'C♭': 'B' };
var primary_sharps   = ['C',  'C♯', 'D', 'D♯', 'E', 'F',  'F♯', 'G', 'G♯', 'A', 'A♯', 'B'];
var secondary_sharps = ['C',  'C♯', 'D', 'D♯', 'E', 'E♯', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B'];
var tertiary_sharps  = ['B♯', 'C♯', 'D', 'D♯', 'E', 'E♯', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B'];
var primary_flats    = ['C', 'D♭', 'D', 'E♭', 'E',  'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B' ];
var secondary_flats  = ['C', 'D♭', 'D', 'E♭', 'E',  'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'C♭'];
var tertiary_flats   = ['C', 'D♭', 'D', 'E♭', 'F♭', 'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'C♭'];
var sharps           = [primary_sharps, secondary_sharps, tertiary_sharps];
var flats            = [primary_flats, secondary_flats, tertiary_flats];
var ionian_names     = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian'];
var ionian_keys   = ['C', 'C♯', 'D♭', 'D', 'E♭', 'E', 'F', 'F♯', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B', 'C♭'];
var melodic_keys  = ['C', 'C♯', 'D♭', 'D', 'E♭', 'E', 'F', 'F♯',            'A♭', 'A', 'B♭', 'B'      ];
var harmonic_keys = ['C', 'C♯',            'E♭', 'E', 'F', 'F♯',            'A♭', 'A', 'B♭', 'B'      ];
var ionian   = [[2, 'Maj'], [2, 'Min'], [1, 'Min'], [2, 'Maj'], [2, 'Maj'], [2, 'Min'], [1, 'Dim']];
var melodic  = [[2, 'Min'], [1, 'Min'], [2, 'Aug'], [2, 'Maj'], [2, 'Maj'], [2, 'Dim'], [1, 'Dim']];
var harmonic = [[2, 'Min'], [1, 'Dim'], [2, 'Aug'], [2, 'Min'], [1, 'Maj'], [3, 'Maj'], [1, 'Dim']];
function rhythmPermutations(size=8, start=[2, 3, 4]) {
    var upper = intDiv(size, 2)
    var old = []
    var results = []
    for (let i of start) {
        old.push([i])
        if (i == size) {
            results.push([i])
        }
    }
    
    for (_ in xrange(upper, 1)) {
        var tmp = []
        for (let digit of start) {
            for (let tail of old) {
                var perm = [digit, ...tail]
                var sum_perm = sum(perm)
                if (sum_perm == size) {
                    results.push(perm)
                    continue
                }
                if (sum_perm == size - 1) {
                    continue
                }
                if (sum_perm < size) {
                    tmp.push(perm)
                }
            }
        }
        old = tmp
    }
    return results
}
function randomStrumPattern(size=8) {
    function strummer(list_int) {
        var result = []
        for (let x of list_int) {
            result.push('/'.repeat(x))
        }
        return result.join(' ') 
    }
    return strummer(choice(rhythmPermutations(size)))
}    
function padding(strLength) {
    if (strLength == 2) {
        var spaces = "&nbsp;".repeat(2)
    }
    else if (strLength == 1) {
        var spaces = "&nbsp;".repeat(3)
    }
    return spaces
}
function chordsFromKey(key='C', mode_offset=0, mode=ionian, first_pass=true) {
    function assembler(notes) {
        if (!(notes.includes(key))) {
            return [[], 0]
        }
        var start         = notes.indexOf(key)
        var shiftedNotes  = shiftSlice(notes, start)
        var chords        = []
        var idx           = 0
        var chosenMode = shiftSlice(mode, mode_offset)
        for (let chord of chosenMode){
            var note = shiftedNotes[idx]
            var spaces = padding(note.length)
            var fullName = `${note}${spaces}${chord[1]}`
            
            chords.push(fullName)
            idx += chord[0]
        }
        return [chords, lenSetFirstChars(chords)]
    }
    var all_notes  = [sharps, flats]
    if (key.includes('♭')) {       // skips sharps
        all_notes = [flats]
    }
    if (key.includes('♯')) {       // skips flats
        all_notes = [sharps]
    }
    for (let index of xrange(3)) {
        for (let notes of all_notes) {
            var res = assembler(notes[index])
            var chords = res[0]
            var chordsLength = res[1]
            if (chordsLength == 7) {
                return [chords, key]
            }
        }
    }
    if (first_pass) {
        var key = diatonic_notes[key]
        if (key) {
            return chordsFromKey(key, mode_offset, mode, false)
        }
    }
    return [[], key]
}
function randomKey() {
    var key         = choice(ionian_keys)
    var mode_offset = choice(xrange(7))
    var mode_name   = ionian_names[mode_offset]
    var res = chordsFromKey(key, mode_offset, ionian)
    var chords = res[0]
    var key = res[1]
                                    
    if (chords.length == 0) {
        return randomKey()
    }
                      
    return [chords, `${key} ${mode_name}`]
}
function chartFromNumbers(chords){
    var numbers = chordNumbers(12)
    var progression = []
    for (let i of numbers) {
        progression.push(chords[i -1])
    }
    return progression
}
function chordNumbers(count=12) {
    var result = []
    var weights = chordWeights(count)
    for (let i of xrange(weights.length)) {
        if (i === 0 || i === count -1) {
            result.push(1)
        }
        else { 
            result.push(choice(weights[i]))
        }
    }
    return result
}
function chordWeights(count=12) {
    function manip(prev) {
        var magic_number = choice(prev)
        var tmp = deepCopy(prev)
        tmp.push(...xfill(2, magic_number))
        tmp.sort
        return tmp
    }
    var start = [1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7]
    var result = [start]
    
    for (let x in xrange(count -1)) {
            result.push(manip(result[x], x))
    }
    return result
}
function idWrite(id, message) {
    document.getElementById(id).innerHTML = message
}
function writeChartToDoc(chart, step) {
    var rightJoin = "&nbsp;".repeat(7)
    var res = ""
    for (let stringIndex in chart) {
        var index = Number(stringIndex) +1
        res += chart[index -1] 
        if (index % step === 0) {
            if (index != chart.length) {
                res += "<br><br>"
            }
            continue
        }
        res += rightJoin
    }
    idWrite("chart", res)
}
function writeRandomChart() {
    var res = randomKey()
    var chords = res[0]
    var key = res[1]
    var chart = chartFromNumbers(chords)
    var strum = randomStrumPattern()
    idWrite("chartStats", `Key: ${key}<br>Rhythm: ${strum}`)
    writeChartToDoc(chart, 4)       
}
writeRandomChart()
