#include <Python.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    PyObject *item;
    int i;

    printf("Size of the Python List = %ld\n", size);
    printf("Allocated = %ld\n", PyList_GET_SIZE(p));

    for (i = 0; i < size; i++)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %d: ", i);

        if (PyString_CheckExact(item))
            printf("str\n");
        else if (PyInt_CheckExact(item))
            printf("int\n");
        else if (PyFloat_CheckExact(item))
            printf("float\n");
        else if (PyTuple_CheckExact(item))
            printf("tuple\n");
        else if (PyList_CheckExact(item))
            printf("list\n");
        else if (PyDict_CheckExact(item))
            printf("dict\n");
        else if (PyBytes_CheckExact(item))
            printf("bytes\n");
        else if (PyUnicode_CheckExact(item))
            printf("unicode\n");
        else if (PySet_CheckExact(item))
            printf("set\n");
        else if (PyDict_CheckExact(item))
            printf("dict\n");
        else if (PySlice_CheckExact(item))
            printf("slice\n");
        else if (PyBool_CheckExact(item))
            printf("bool\n");
        else if (PyNone_CheckExact(item))
            printf("None\n");
        else
            printf("Unknown type\n");
    }
}
