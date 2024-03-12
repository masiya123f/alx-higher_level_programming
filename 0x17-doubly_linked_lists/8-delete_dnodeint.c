#include "lists.h"

/**
 * delete_dnodeint_at_index - deletes the node at index of a dlistint_t linked list
 * @head: pointer to the head of the list
 * @index: index of the node that should be deleted
 *
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *current = *head;
    dlistint_t *temp = NULL;
    unsigned int i = 0;

    if (*head == NULL)
        return -1;

    if (index == 0)
    {
        *head = (*head)->next;
        free(current);
        if (*head != NULL)
            (*head)->prev = NULL;
        return 1;
    }

    while (current != NULL && i < index)
    {
        temp = current;
        current = current->next;
        i++;
    }

    if (current == NULL)
        return -1;

    temp->next = current->next;
    if (current->next != NULL)
        current->next->prev = temp;
    free(current);
    return 1;
}

