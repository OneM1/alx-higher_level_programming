#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info -Function to print information about a Python list
 * @p: A pointer to the Python list (PyObject)
 */
void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size = PyList_Size(p);
Py_ssize_t allocated = list->allocated;
Py_ssize_t i;

printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", allocated);

for (i = 0; i < size; ++i)
{
printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
}
