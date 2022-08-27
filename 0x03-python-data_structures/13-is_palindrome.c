#include "lists.h"

/**
 * is_palindrome - checking if the list is a palindrome
 * @head: the pointer to the point head of the list
 * return: true if it is and false if it isn't
 */

int is_palindrome(listint_t **head)
{
	listnt_t *slow, *fast, mid_list;
	int n;

	*slow = *fast =	*head
