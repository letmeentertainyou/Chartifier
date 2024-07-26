/* 
    This is a portable resizable Array library built with and the ability to import regular C arrays 
    into an Array struct. This version stores an array of unsigned chars (Byte) in Array->values.
*/

#include "array.h"
/* Returns the value stored in the index if 0 < index <= length, otherwise probably breaks. */
int unpack(Array* array, int index) {
    return array->values[index];
}

/* Resets all the filled values in the array to zero and resets array->length to zero. */
void clear_array(Array* array) {
    memset(array->values, 0, array->length * sizeof(Byte));
    array->length = 0;
}

/* Initializes an empty Array of size=size. */
Array *empty_array(int size) {
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
    memcpy(new_array->values, array->values, array->length * sizeof(Byte));
    free(array);
    return new_array;
}

/* Appends an 8 bit value into the array and resizes it if it's full. */
Array *append(Array *array, int value) {
    if (array->length < array->size) {
        array->values[array->length] = (Byte)value;
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
        target = append(target, copy->values[i]);
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
        printf("%d ", array->values[i]);
    }
    printf("\n");
}

/* Returns the sum of an Array struct. */
int sum_array(Array *array) {
    int sum = 0;
    for (int i = 0; i < array->length; i++) {
        sum += array->values[i];
    }
    return sum;
}

/* Shows the values of size, length fields of the array for debugging. */
void inspect(Array *array) {
    printf("size: %i, length: %i.\n", array->size, array->length);
}

/* Allows me to print an int and a new line with way less syntax for debugging. */
void println(int i) {
    printf("%i\n", i);
}