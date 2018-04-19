#include "Python.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *lst = (PyListObject *) p;
	long long ct = -1, size;

	size = (long long) Py_SIZE(p);
	printf("[*] Size of the Python List = %lld\n", size);
	printf("[*] Allocated = %lld\n", (long long) lst->allocated);
	while (++ct < size)
		printf("Element %lld: %s\n", ct, Py_TYPE(lst->ob_item[ct])->tp_name);
}
