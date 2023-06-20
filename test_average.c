#include "main.h"

int main ()
{
	int array1[] = {7,4,3,9,1,8,5,2,6};
	int array2[] = {100000};
	int array3[] = {8};
	int k1=3, k2=0, k3=100000;
	int *o_array1, *o_array2, *o_array3;

	printf("input:\n");
	print_array(array1);
	printf("output:\n");
	o_array1 = getAverages(array1, k1);
	print_array(o_array1);

	printf("\ninput:\n");
        print_array(array2);
        printf("output:\n");
        o_array2 = getAverages(array2, k2);
        print_array(o_array2);

	printf("\ninput:\n");
        print_array(array3);
        printf("output:\n");
        o_array1 = getAverages(array3, k3);
        print_array(o_array3);
}
