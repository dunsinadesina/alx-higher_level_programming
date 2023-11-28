#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - function to insert node to linked list
 * @head: pointer to pointer parameter beginning of list
 * @number: parameter
 *
 * Return: new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new;

	node = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}
	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
