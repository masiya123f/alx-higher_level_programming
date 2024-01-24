#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyListObject *list = (PyListObject *)p;

    printf("[*] Python list info\n");
    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
        if (PyBytes_Check(list->ob_item[i])) {
            print_python_bytes(list->ob_item[i]);
        }
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = (unsigned char *)PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %d bytes: ", size > 10 ? 10 : (int)size);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", str[i]);
        if (i < 9 && i < size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}

