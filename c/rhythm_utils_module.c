/* 
    I figured out how to raise a MemoryError in Python when there is an allocation returns NULL but I also
    learned that represents a very tiny amount of memory errors and that this program will crash pretty easily
    with a huge input size and it doesn't seem to raise the memory error. So I need to learn a lot more about
    allocation in C and how I can best optimize this code so that it crashes more elegantly.

    I did notice that my code crashes in Python on a use case that doesn't crash C so now I'm curious about
    how much memory the Python interpreter is using even when it's running C code. It might just be the nature
    of returning the large results array to Python that is causing such a huge overflow. I will look in to it.

    I was hoping that putting all of this back into Python would allow me to benchmark the original Python code
    against this module so I can see what kind of performance improvements I got but I still need to get my memory
    management figured out before that step.
*/

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "rhythm_utils.h"

static PyObject* RhythmError;

static PyObject* permutations(PyObject* self, PyObject* args) {
    int size;
    if (!PyArg_ParseTuple(args, "i", &size)) {
        return NULL;
    }

    Array *array = rhythm_permutations(size);
    PyObject* py_list = PyList_New(array->length);
    if (!py_list) {
        return NULL;
    }

    for (int i = 0; i < array->length; i++) {
        PyObject* py_int = PyLong_FromLong(unpack(array, i));
        if (!py_int) {
            Py_DECREF(py_list);
            return NULL;
        }
        PyList_SetItem(py_list, i, py_int);
    }
    free(array);
    return py_list;
}

static PyMethodDef RhythmMethods[] = {
    {
        // This is the external name of the method.
        "permutations",
        // This is the internal name of the method, they don't have to match.
        permutations,
        METH_VARARGS,
        "Calculate the rhythmic permutations of a given size and return a one dimensional list.\n",
    },
    {NULL, NULL, 0, NULL},  // This means all the methods have been defined.
};

static PyModuleDef rhythmmodule = {
    PyModuleDef_HEAD_INIT,
    "rhythm",
    "Inspired by the example Spam module.",
    -1,
    RhythmMethods,
};

PyMODINIT_FUNC PyInit_rhythm_utils() {
    PyObject* module;

    module = PyModule_Create(&rhythmmodule);
    if (module == NULL) {
        return NULL;
    }
    RhythmError = PyErr_NewException("rhythm.Error", NULL, NULL);
    Py_INCREF(RhythmError);
    PyModule_AddObject(module, "Error", RhythmError);
    return module;
}