#include <Python.h>

/**
 * print_python_string - Prints detailed information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p) {
    printf("[.] string object info\n");

    // Type Check and Early Return for Efficient Error Handling
    if (!PyUnicode_Check(p)) {  
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // Handling ASCII vs. Unicode  
    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        printf("  type: compact ascii\n");
        printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));  
        printf("  value: %s\n", (char *)PyUnicode_DATA(p)); // Casting for ASCII output
    } else {
        printf("  type: compact unicode object\n");
        printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));

        // UTF-8 Conversion with 'const' correctness
        const char *utf8_str = PyUnicode_AsUTF8(p);
        printf("  value: %s\n", utf8_str); 

        // Memory cleanup (safe 'const' handling)
        char *tmp = (char *)utf8_str; 
        PyMem_Free(tmp); 
    }
}
