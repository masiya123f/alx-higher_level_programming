#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);

    new_node->n = number;

    if (!*head || (*head)->n >= number)  /* Insert at beginning if list is empty or number is smaller than head node */
    {
        new_node->next = *head;
        *head = new_node;
    }
    else  /* Insert in correct sorted position */
    {
        listint_t *node = *head;
        while (node->next && node->next->n < number)
            node = node->next;

        new_node->next = node->next;
        node->next = new_node;
    }

    return (new_node);
}

