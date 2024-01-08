#include <stddef.h>
#include "lists.h"

/**
 * reverse_list - Function to reverse a linked list
 * @head: Pointer to the head of the linked list
 * Return: Pointer to the head of the reversed list
 */

listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *current = head, *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * is_palindrome - Checks singly_linked_list is a palindrome or not
 * @head: Pointer to the head of the linked list
 * Return: 1 if the list is a palindrome, 0 else
 */

int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow = *head, *fast = *head;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    slow = reverse_list(slow);
    fast = *head;

    while (slow != NULL)
    {
        if (slow->n != fast->n)
            return 0;
        slow = slow->next;
        fast = fast->next;
    }

    return 1;
}

