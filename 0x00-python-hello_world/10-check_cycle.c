#include "lists.h"


/**
* check_cycle - checks if there is a loop in a cycle
* @list: head pointer
* Return: 0 or 1
*/

int check_cycle(listint_t *list)
{
	listint_t *p, *q;

	p = list;
	q = list;
	while (q && q->next)
	{
		p = p->next;
		q = q->next->next;
		if (p == q)
			return (1);
	}
	return (0);
}
