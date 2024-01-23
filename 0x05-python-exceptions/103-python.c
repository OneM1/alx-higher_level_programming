#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *element;

    printf("[*] Python list info\n");
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        if (PyBytes_Check(element)) {
            printf("[.] bytes object info\n");
            printf("  size: %ld\n", PyBytes_GET_SIZE(element));
            printf("  trying string: %s\n", PyBytes_AsString(element));
            printf("  first %ld bytes: ", (PyBytes_GET_SIZE(element) > 10) ? 10 : PyBytes_GET_SIZE(element));
            for (Py_ssize_t j = 0; j < ((PyBytes_GET_SIZE(element) > 10) ? 10 : PyBytes_GET_SIZE(element)); ++j) {
                printf("%02x ", (unsigned char)PyBytes_AS_STRING(element)[j]);
            }
            printf("\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first %ld bytes: ", (size > 10) ? 10 : size);
    for (Py_ssize_t i = 0; i < ((size > 10) ? 10 : size); ++i) {
        printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    printf("[.] float object info\n");
    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
}

