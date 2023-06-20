#include "main.h"


/**
 * print_array - function that print all the elements of an array
 *
 * @array: array we want to print the elements
 *
 * Return: Nothing
 */


void print_array(int *array)
{
	unsigned int i;

	printf("[");
	for (i = 0; i < sizeof(array1); i++)
	{
		printf("%d, ", array[i]);
	}
	printf("]");
}
