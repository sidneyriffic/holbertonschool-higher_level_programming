#include "lists.h"

/**
 * insert_node - inserts a node at start of a listint list
 *
 * @head: start of listint list
 * @number: value to add
 *
 * Return: address of new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;

	if (head == NULL)
		return (NULL);
	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
		return (NULL);
	ptr->n = number;
	ptr->next = *head;
	*head = ptr;
	return (ptr);
}
