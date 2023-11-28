#include "lists.h"
/**
 * insert_node - function to insert node to linked list
 * @head: pointer to pointer parameter beginning of list
 * @number: parameter
 *
 * Return: new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *previous;

	new_node = add_nodeint_end(number);
	if (new_node == NULL)
		return (NULL);
	current = *head;
	previous = NULL;
	while (current != NULL && current->data < number)
	{
		previous = current;
		current = current->next;
	}
	if (previous == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		previous->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
