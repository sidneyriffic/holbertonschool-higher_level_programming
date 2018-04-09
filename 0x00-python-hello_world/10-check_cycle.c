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
	listint_t *ptr = list, *end;

	if (list == NULL)
		return (0);
	end = ptr->next;
	while (1)
	{
		if (end == ptr)
			return (1);
		if (end->next == NULL)
			return (0);
		end = end->next;
		if (end->next == NULL)
			return (0);
		end = end->next;
		ptr = ptr->next;
	}
}
