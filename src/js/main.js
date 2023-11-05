'use strict'

/* RHYTHM */

/*
    Strum patterns are defined in the file js/strumPatterns.js, this function randomly
    picks a strum pattern and makes it human readable. If size isn't a valid strumPatterns
    key things will crash. 
*/
function randomStrumPattern(size=8){
    /* 
        This replaces ints with slashes for the strum pattern.
    */
    function strummer(list_int) {
        var result = []
        for (let x of list_int) {
            result.push('/'.repeat(x))
        }
        return result.join(' ') 
    }
    return strummer(choice(strumPatterns[size]))
}    

/* ########## HARMONY ##########  */

/*
    This is just to make the chords prettier on the html page, it does not exist in
    the python source code.
*/

function padding(strLength) {
    if (strLength == 2) {
        var spaces = "&nbsp;".repeat(2)
    }
    else if (strLength == 1) {
        var spaces = "&nbsp;".repeat(3)
    }
    return spaces
}


/*
    This function takes a key, a mode_offset(0 to 6) and a mode, and tries to
    load a set of keys. If it fails on the first pass it will try again with
    a diatonic alternative for the key. So it might try Gb maj if F# fails (F# won't fail)]

    With the data in musicTheory.js this function is extremely capable of finding lots of 
    weird keys. I don't even know what the modes for melodic/harmonic mind are called but this
    supports most of them.
*/
function chordsFromKey(key='C', mode_offset=0, mode=ionian, first_pass=true) {

    /*
        This function takes a give set of notes, and attempts to build some chords out of it
        the outer function confirms that the lenSetFirstChars assembler returns is 7. 
        
        assembler is called until it returns a seven or there are no more note pools to draw from.
    */
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

/*
    Picks a random key and random variation of the ionian mode (harmonic/melodic could be
    used instead), then loads up the chords from that key/mode. If randomKey gets an invalid
    key for some reason (rare), it just keeps trying until a valid key is found.
*/
function randomKey() {
    var key         = choice(ionian_keys)
    var mode_offset = choice(xrange(7))
    var mode_name   = ionian_names[mode_offset]
    var res = chordsFromKey(key, mode_offset, ionian)
    var chords = res[0]
    var key = res[1]
                                    
    // Empty arrays aren't falsey is JS so we need to check the length
    if (chords.length == 0) {
        return randomKey()
    }
                      
    return [chords, `${key} ${mode_name}`]

}

/* RANDOM CHORD CHART MATH */

/*
    This generates some chord numbers and then applies them to a given set of chords.
*/
function chartFromNumbers(chords){
    var numbers = chordNumbers(12)
    var progression = []

    for (let i of numbers) {
        progression.push(chords[i -1])
    }
    return progression
}

/*
    This chooses x chords at random, and generates some additional weighting info for those chords too.
    This function also forces the first and last chord of a progression to be the one chord. This is a
    common music theory practice but it can be removed for more random charts.
*/
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

/*
    This generates some random weights for whatever length of chord chart you want.
    This is just my first go at this math and I won't change it until the website is a
    bit nicer so I can freeze this version of the algorithm.

    There are many flaWs with this version, namely that a chord can appear too many times
    in a row. But actually that needs to be solved in the function above.

*/
function chordWeights(count=12) {
    /*
        Picks a number from the current set of weights and adds two more of that number.
    */
    function manip(prev) {
        var magic_number = choice(prev)
        var tmp = deepCopy(prev)
        tmp.push(...xfill(2, magic_number))
        tmp.sort
        return tmp
    }

    // These are not zero indexed so that they are readable by human musicians.
    var start = [1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7]
    var result = [start]
    
    for (let x in xrange(count -1)) {
            result.push(manip(result[x], x))
    }
    return result
}

/* HTML */

/* 
    This function allows you to overwrite any element by id in the document.
*/
function idWrite(id, message) {
    document.getElementById(id).innerHTML = message
}

/*
    Takes a set of chords, and an integer representing how many chords show go in a row,
    then it writes the chords to the doc. This is for after you generated a chart with
    chartFromNumbers
*/
function writeChartToDoc(chart, step) {
    var rightJoin = "&nbsp;".repeat(7)
    var res = ""
    for (let stringIndex in chart) {
        var index = Number(stringIndex) +1
        res += chart[index -1] 
        if (index % step === 0) {
            // Add two new lines at the step, unless it's the last line.
            if (index != chart.length) {
                res += "<br><br>"
            }
            // This continue skips writing whitespace to the end of the lines.
            continue
        }
        res += rightJoin
    }
    idWrite("chart", res)
}

/*
    This function generates some random chords, and a random chart, and a random strum
    pattern, and puts all the pieces together.
    
    When the radio buttons are added there will need to be a version of this function that
    checks the radio buttons before randomly generating those things. If for instance the key
    of C minor is selected then a random key is not needed anymore.

    This function is called every time the page is loaded, and when a 'New Chords' is added 
    to the html page then this function is what that button will call. 
*/
function writeRandomChart() {
    var res = randomKey()
    var chords = res[0]
    var key = res[1]
    var chart = chartFromNumbers(chords)
    var strum = randomStrumPattern()

    idWrite("topBar", `Key: ${key}<br>Rhythm: ${strum}<br>`)
    writeChartToDoc(chart, 4)       
}

/*
    This is what the NEW CHART button will call. 
*/
function cleanWrite() {
    writeRandomChart()
}

// First write to the document needs to be explicit.
writeRandomChart()

