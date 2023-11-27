#include "lists.h"
/**
 * check_cycle - function to check for cycle in linked list
 * @list: pointer parameter
 *
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *beginning, *end;

	if (list == NULL || list->next == NULL)
		return (0);
	beginning = list;
	end = list->next;
	while (end != NULL && end->next != NULL)
	{
		if (beginning == end)
			return (1);
		beginning = beginning->next;
		end = end->next->next;
	}
	return (0);
}
