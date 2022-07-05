#include "lists.h"

/**
* is_palindrome -  check if a linked list is palindrome
* @node: head pointer
* Return: 1 or 0
**/

listint_t *reverse_list(listint_t *node);

int is_palindrome(listint_t **head)
{
	listint_t *p, *q;

	if (*head == NULL)
		return (1);

	p = *head;
	q = *head;

	while (q->next && q->next->next)
	{
		p = p->next;
		q = q->next->next;
	}
	p = reverse_list(p);
	q = *head;

	while (p != NULL && q != NULL)
	{
		if (p->n != q->n)
			return (0);
		p = p->next;
		q = q->next;
	}
	return (1);
}

/**
* reverse_list - reverse a linked list
* @node: head pointer
* Return: head pointer
*/

listint_t *reverse_list(listint_t *node)
{
	listint_t *currentnode, *nextnode, *prevnode;

	prevnode = NULL;
	currentnode = nextnode = node;

	while (nextnode != NULL)
	{
		nextnode = nextnode->next;
		currentnode->next = prevnode;
		prevnode = currentnode;
		currentnode = nextnode;
	}
	node = prevnode;
	return (node);
}
