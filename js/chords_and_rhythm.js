'use strict'

/* ########## HARMONY ##########  */

function chordsFromKey(key='C', mode_offset=0, mode=ionian, first_pass=true) {

    function assembler(notes) {
        if (!(notes.includes(key))) {
            return [[], 0]
        }
        var start         = notes.indexOf(key)
        var shiftedNotes  = shiftSlice(notes, start)
        var chords        = []
        var idx           = 0
                     // This remaps the mode to the offset you picked
        var chosenMode = shiftSlice(mode, mode_offset)
        for (let chord of chosenMode){
            chords.push(`${shiftedNotes[idx]} ${chord[1]}`)
            idx += chord[0]
        }
        return [chords, lenSetFirstChars(chords)]
    }

    var all_notes  = [sharps, flats]
    if (key.includes('b')) {       // skips sharps
        all_notes = [flats]
    }
    if (key.includes('#')) {       // skips flats
        all_notes = [sharps]
    }

    for (let index=0;index<3;index++) {
        for (let notes of all_notes) {
            var res = assembler(notes[index])
            var chords = res[0]
            var chord_len = res[1] 
            if (chord_len == 7) {
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

function randomChords() {
    var key         = choice(ionian_keys)
    var mode_offset = choice(xrange(7))
    var mode_name   = ionian_names[mode_offset]
    var res = chordsFromKey(key, mode_offset, ionian)
    var chords = res[0]
    var key = res[1]
                                    
    // Empty arrays aren't falsey is JS so we need to check the length
    if (chords.length == 0) {
        return randomChords()
    }
                      
    return [chords, `${key} ${mode_name}`]

}

// Not random yet, just 12 bars. Still rad!
function randomChordChartt(chords){
    var twelve_bar = [1, 1, 1, 1, 4, 4, 1, 1, 4, 1, 4, 5]
    var progression = []
    for (let i of twelve_bar){
        progression.push(chords[i-1])
    }
    return progression
}

/* ########## RHYTHM ##########  */

// This just does my slashes for the strum pattern
function strummer(list_int) {
    var result = []
    for (let x of list_int){
        result.push('/'.repeat(x))}
    return result.join(' ') 
}

function eighthNotePool(size, upper) {
    var pool = []
    for (let i=2; i<=upper; i++) {
        pool.push(...Array(intDiv(size, i)).fill(i))
    }
    return pool
}

function uniqueCombos(size, pool) {
    var combos = []
    for (let i=pool.length; i>=0; i--)  {
        for (let combo of combinations(pool, i)) {
            if (sum(combo) == size){
                combos.push(combo)   
                // Grab the reverse right now
                combos.push(Array.from(combo).reverse())
            }
        }
    }
    return removeDupeArrays(combos)
}

// Generate random size/upper for more variations on rhythm.
function randomStrumPattern(size=8, upper=4) {
    var pool = eighthNotePool(size, upper)
    var combos = uniqueCombos(size, pool)
    var result = choice(combos)
    return strummer(result)
}

/* ########## HTML ##########  */

function writeChordsToDoc(chords, step) {
    var rightJoin = "&nbsp;".repeat(7)
    for (index in chords) {
        var index = Number(index) +1
        document.write(`${chords[index -1]}${rightJoin}`)
                                        // No trailing newline.
        if (index % step === 0 && index != chords.length) {
            document.write("<br>")
        }
    }
}

function writeRandomChords() {
    var res = randomChords()
    var chords = res[0]
    var key = res[1]
    var chart = randomChordChartt(chords)
    var strum = randomStrumPattern()
    document.write(`Key: ${key}<br>`)
    document.write(`Strum pattern: ${strum}<br>`)
    writeChordsToDoc(chart, 4, key)       
}

writeRandomChords()
