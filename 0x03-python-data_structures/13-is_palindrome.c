#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

size_t listint_len(const listint_t *h)
{
    size_t length = 0;
    while (h != NULL)
    {
        length++;
        h = h->next;
    }
    return length;
}

int is_palindrome(listint_t **head)
{
    listint_t *start = NULL, *end = NULL;
    unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

    if (head == NULL || *head == NULL)
        return (1);

    start = *head;
    len = listint_len(start);
    len_cyc = len * 2;
    len_list = len_cyc - 2;
    end = *head;

    for (; i < len_cyc; i = i + 2)
    {
        if (start[i].n != end[len_list].n)
            return (0);

        len_list = len_list - 2;
    }

    return (1);
}
