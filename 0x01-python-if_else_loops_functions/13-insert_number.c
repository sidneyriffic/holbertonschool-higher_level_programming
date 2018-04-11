#include "lists.h"

/**
 * insert_node - inserts a node in a sorted listint list
 *
 * @head: start of listint list
 * @number: value to add
 *
 * Return: address of new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	ptr = *head;
	if(ptr != NULL && ptr->n < number)
	{
		while(ptr->next != NULL && ptr->next->n < number)
			ptr = ptr->next;
		new->next = ptr->next;
		ptr->next = new;
	}
	else
	{
		new->next = *head;
		*head = new;
	}
	new->n = number;
	return (new);
}
