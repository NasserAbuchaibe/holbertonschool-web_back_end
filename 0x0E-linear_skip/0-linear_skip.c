#include "search.h"

/**
 * linear_skip - function that searches for a value in a sorted 
 * skip list of integers
 * @list: pointer to head of skip list
 * @value: is the value to search fo
 *
 * Return: pointer on success or NULL
 */

skiplist_t *linear_skip(skiplist_t *list, int value)
{
	skiplist_t *exp_l, *prev;

	if (!list)
		return (NULL);

	exp_l = list->express;
	prev = list;

	for (; exp_l; exp_l = exp_l->express)
	{
		printf("Value checked at index [%lu] = [%d]\n",
				exp_l->index, exp_l->n);
		if (!exp_l->express || exp_l->n >= value)
		{
			if (!exp_l->express && exp_l->n < value)
			{
				prev = exp_l;
				for (; exp_l->next; exp_l = exp_l->next)
					;
			}
			printf("Value found between indexes [%lu] and [%lu]\n",
					prev->index, exp_l->index);
			for (; prev; prev = prev->next)
			{
				printf("Value checked at index [%lu] = [%d]\n",
						prev->index, prev->n);
				if (prev->n > value)
					return (NULL);
				if (prev->n == value)
					return (prev);
			}
			break;
		}
		prev = exp_l;
	}
	return (NULL);
}
