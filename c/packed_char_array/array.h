#ifndef ARRAY_H_
#define ARRAY_H_

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned char Byte;
struct ARRAY {
    int size;
    int length;
    Byte values[];
};

typedef struct ARRAY Array;
Byte pack(Byte byte, int pos, int value);
int unpack(Array *array, int index);
void clear_array(Array* array);
Array *empty_init(int size);
Array *resize_array(Array *array);
Array *append(Array *array, int value);
Array *append_pad(Array *array, int value);
Array *int_init(int value);
Array *array_init(int copy[], int copy_length);
Array *extend(Array *target, Array *copy);
Array *extend_pad(Array *target, Array *copy);
void print_array(Array *array);
int sum_array(Array *array);
void inspect(Array *array);
void println(int i);
#endif