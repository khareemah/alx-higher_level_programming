#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* insert_node - inserts a node in a sorted list
* @head: head pointer of the list
* @number: value of node to insert
* Return: address to the newnode or NULL if it fails
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	
	if(*head == NULL)
		*head = newnode;
	temp = *head;

	if(temp->next == NULL)
	{
		if(temp->n > newnode->n)
		{
			newnode->next = *head;
			*head = newnode;
		}
		else
			temp->next = newnode;
			
	}
	else
	{
		while (temp->next->n < newnode->n)
			temp = temp->next;
		newnode->next = temp->next;
		temp->next = newnode;
	}

	return (newnode);
}
