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
	if(ptr != NULL)
	{
		while(ptr->next != NULL && ptr->next->n < number)
			ptr = ptr->next;
		if (ptr->n >= number)
			ptr=ptr->next;
	}
	new->n = number;
	new->next = ptr;
	if (ptr == *head)
		*head = new;
	return (new);
}
