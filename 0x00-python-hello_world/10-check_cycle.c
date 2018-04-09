#include "lists.h"

/**
 * check_cycle - checks if listint_t list loops on itself
 *
 * @list: list to check for loops
 *
 * Return: 1 if loops, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *end;

	if (list == NULL)
		return (0);
	ptr = list;
	end = ptr->next;
	if (end == NULL)
		return (0);
	while (1)
	{
		if (end == ptr)
			return (1);
		end = end->next;
		if (end == NULL)
			return (0);
		end = end->next;
		if (end == NULL)
			return (0);
		ptr = ptr->next;
	}
}
