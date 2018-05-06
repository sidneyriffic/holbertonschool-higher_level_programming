#include <stdio.h>
#include <locale.h>
#include "Python.h"

void print_python_string(PyObject *p)
{
	PyASCIIObject *ascobj = (PyASCIIObject *) p;
	wchar_t *buffer;
	Py_ssize_t size;

	setlocale(LC_ALL, "");
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (ascobj->state.ascii == 1)
	{
		printf("  type: compact ascii\n");
		printf("  length: %lld\n", (long long) ascobj->length);
		printf("  value: %s\n", (char *) (ascobj + 1));
	}
	else if (ascobj->state.compact == 1)
	{
		printf("  type: compact unicode object\n");
		printf("  length: %lld\n", (long long) ascobj->length);
		buffer = PyUnicode_AsWideCharString(p, &size);
		printf("  value: %ls\n", buffer);
		PyMem_Free(buffer);
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
