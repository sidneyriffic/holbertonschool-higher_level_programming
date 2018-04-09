#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *ptr = list, *end;

	if (list == NULL)
		return (0);
	while (1)
	{
		end = ptr->next;
		if (end == NULL)
			return (0);
		ptr = list;
		while (ptr != end)
		{
			if (ptr == end->next)
				return(1);
			ptr = ptr->next;
		}
	}
}
