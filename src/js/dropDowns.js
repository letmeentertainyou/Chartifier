/* 
    All the functions/constants required for the dropdown menus.
*/

const countSelect = document.getElementById("count");
const modeSelect = document.getElementById("modes");
const noteSelect = document.getElementById("notes");

const counts = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];

function populateCounts() {
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
    while (noteSelect.firstChild) {
        noteSelect.removeChild(noteSelect.firstChild);
    }

    notes = [];
    if (mode == "Melodic") {
        notes = melodic_keys;
    } else if (mode == "Harmonic") {
        notes = harmonic_keys;
    } else {
        notes = ionian_keys;
    }

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
