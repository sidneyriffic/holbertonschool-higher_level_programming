#include "Python.h"
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes - print information about a bytes object
 *
 * @p: bytes object
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *) p;
	int len;
	char *ptr;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = PyBytes_Size(p);
	ptr = bytes->ob_sval;
	printf("  size: %d\n  trying string: %s\n", len, bytes->ob_sval);
	len++;
	if (len > 10)
		len = 10;
	printf("  first %d bytes:", len);
	while (len--)
		printf(" %.2x", (unsigned char) *ptr++);
	printf("\n");
}

/**
 * print_python_list - prints information about a python list
 * and extra info on bytes objects
 *
 * @p: list to print information about
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyListObject *lst = (PyListObject *) p;
	long long ct = -1, size;
	const char *type;

	printf("[*] Python list info\n");
	size = (long long) PyList_Size(p);
	printf("[*] Size of the Python List = %lld\n", size);
	printf("[*] Allocated = %lld\n", (long long) lst->allocated);
	while (++ct < size)
	{
		type = lst->ob_item[ct]->ob_type->tp_name;
		printf("Element %lld: %s\n", ct, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(lst->ob_item[ct]);
	}
}
