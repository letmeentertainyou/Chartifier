/* 
    This is for the js required for dropdown menus. When it is complete it can be brought into a different file.

    Change all names to match musicTheory, then remove month logic, then
    make simple drop downs. Then follow up harmonic logic.
*/

// Use these variables in the chart gen function.
// If they are falsey then randomly generate the key/mode
// If they aren't then use them,

// What happens if mode or key is falsey? Random, They both have to be
// selected for user input. Maybe put a message that only one is selected
// But that's advanced stuff.
const countSelect = document.getElementById("count");
const modeSelect = document.getElementById("modes");
const noteSelect = document.getElementById("notes");

const counts = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];

function populateCounts() {
    //Get the current year as a number
    //Make the previous 100 years be an option
    for (let x of counts) {
        const option = document.createElement("option");
        option.textContent = x;
        countSelect.appendChild(option);
    }
    countSelect.value = "";
}

//Modes are always the same
function populateModes() {
    for (let x of modes) {
        const option = document.createElement("option");
        option.textContent = x;
        modeSelect.appendChild(option);
    }
    modeSelect.value = "";
}

function populateNotes(mode) {
    //Delete all of the children of the day dropdown
    //if they do exist
    while (noteSelect.firstChild) {
        noteSelect.removeChild(noteSelect.firstChild);
    }

    notes = [];
    // Fill this out later
    if (mode == "Melodic") {
        notes = melodic_keys;
    } else if (mode == "Harmonic") {
        notes = harmonic_keys;
    } else {
        notes = ionian_keys;
    }
    // do an xrange for the length of notes.
    for (let x of notes) {
        const option = document.createElement("option");
        option.textContent = x;
        noteSelect.appendChild(option);
    }
    noteSelect.value = "";
}

populateCounts();
populateModes();
populateNotes(modeSelect.value);

modeSelect.onchange = function () {
    populateNotes(modeSelect.value);
};
