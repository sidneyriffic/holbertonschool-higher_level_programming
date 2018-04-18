#include "lists.h"

listint_t *is_pal_recurs(listint_t *left, listint_t *right)
{
	if (right->next == NULL)
		return (left->next);
	right = right->next;
	if (right->next == NULL)
	{
		if (left->n != left->next->n)
			return (NULL);
		if (left->next->next == NULL)
			return (left);
		return (left->next->next);
	}
	right = is_pal_recurs(left->next, right->next);
	if (right == NULL)
		return (NULL);
	if (right->n == left->n)
	{
		if (right->next == NULL)
			return (left);
		return (right->next);
	}
	return (NULL);
}
		

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	if (is_pal_recurs(*head, *head) != NULL)
		return (1);
	return (0);
}
