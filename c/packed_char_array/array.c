/* 
    This is a portable resizable Array library built with and the ability to import regular C arrays 
    into an Array struct. This version stores an array of unsigned chars (Byte) in Array->values and
    packs four two bit values into each Byte.
*/

#include "array.h"

int PACK_MAP[5] = {0, 0, 1, 2, 3};
int UNPACK_MAP[4] = {0, 2, 3, 4};

/* This packs the bit pair at pos with a value from 0-3. The input value should be in [0, 2, 3, 4]. */
Byte pack(Byte byte, int pos, int value) {
    int shift = 6 - (pos * 2);
    Byte mask = 3 << shift;
    return (byte & ~mask) | ((PACK_MAP[value] << shift) & mask);
}

/* Returns the value stored in the index if 0 < index <= length, otherwise probably breaks. */
int unpack(Array* array, int index) {
    return UNPACK_MAP[(array->values[index / 4] >> (6 - (index % 4 * 2))) & 3];
    /* Readable version of the above code.
    int shift = 6 - (index % 4 * 2);
    int key = (array->values[index / 4] >> shift) & 3;
    return UNPACK_MAP[key]; //*/
}

/* Resets all the filled values in the array to zero and resets array->length to zero. */
void clear_array(Array* array) {
    memset(array->values, 0, (array->length / 4) * sizeof(Byte));
    array->length = 0;
}

/* Initializes an empty Array of size=size. */
Array *empty_array(int size) {
    // For some reason malloc + this library + -O flags caused a leak and calloc does not.
    Array *array = (Array *)calloc(1, sizeof(Array) + size * sizeof(Byte));
    if (!array) {
        PyErr_SetString(PyExc_MemoryError, "Unable to allocate memory for array.");
        free(array);
        return NULL;
    }
    *array = (Array){size, 0};  // This sets the size and length fields.
    return array;
}

/* Copies the contents of the array into a new one of new_size, and then frees original array. */
Array *resize_array(Array *array) {
    Array *new_array = empty_array(array->size * 2);
    new_array->length = array->length;
    memcpy(new_array->values, array->values, (array->length / 4) * sizeof(Byte));
    free(array);
    return new_array;
}

/* Takes a value in as 0, 2, 3, 4 and appends it into an Array. Resizes it if it's full.*/
Array *append(Array *array, int value) {
    int length = array->length / 4;
    if (length < array->size) {
        array->values[length] = pack(array->values[length], array->length % 4, value);
        array->length++;
        return array;
    } else {
        return append(resize_array(array), value);
    }
}

/* This appends one value and pads it with a zero. */
Array *append_pad(Array *array, int value) {
    return append(append(array, value), 0);
}

/* Initializes an Array with the given value in it. */
Array *array_from_int(int value) {
    return append(empty_array(1), value);
}

/* This initializes an Array with a regular C array and it's length. This is different from
   extend() which only takes other Array structs and doesn't initialize. */
Array *array_from_array(int copy[], int copy_length) {
    Array * target = empty_array(copy_length);
    for (int i = 0; i < copy_length; i++) {
        target = append(target, copy[i]);
    }
    return target;
}

/* Iterates over copy and appends each element into target. */
Array *extend(Array *target, Array *copy) {
    for (int i = 0; i < copy->length; i++) {
        target = append(target, unpack(copy, i));
    }
    return target;
}

/* Iterates over copy and appends each element into target then pads with a zero. */
Array *extend_pad(Array *target, Array *copy) {
    return append(extend(target, copy), 0);
}

/* Prints an array in the format x x x x x for easy reading. */
void print_array(Array *array) {
    if (array->length == 0) {
        printf("Can't print an empty array.\n");
        return;    
    }
    for (int i = 0; i < array->length; i++) {
        int value = unpack(array, i);
        printf("%d ", value);
    }
    printf("\n");
}

/* Returns the sum of an Array struct. */
int sum_array(Array *array) {
    int sum = 0;
    for (int i = 0; i < array->length; i++) {
        sum += unpack(array, i);
    }
    return sum;
}

/* Shows the values of length, size, pos, length fields of the array for debugging. */
void inspect(Array *array) {
    int length = array->length / 4;
    int pos = array->length % 4;
    printf("size: %i, len: %i, pos: %i, length: %i.\n", array->size, length, pos, array->length);
}

/* Allows me to print an int and a new line with way less syntax for debugging. */
void println(int i) {
    printf("%i\n", i);
}