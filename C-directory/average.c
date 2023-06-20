#include "main.h"

/**
 * getAverages- function that return an array avgs of length n where
 * avgs[i] is the k-radius average for the subarray centered at index i
 * @nums: 0-indexed array of n integers
 * @k: radius of the subarray
 * Return: an array avgs of length n where avgs[i] is the k-radius average
 * for the subarray centered at index i.
 */

int *getAverages(int *nums, int k)
{
	int *avgs;
	unsigned int i, j, l, m;
	int sum = 0;
	int avg;

	l = i - k;
	m = i + k;

	for (i = 0, i < sizeof(nums), i++)
	{
		if (l < 0 || m > sizeof(nums))
			avgs[i] = -1;
		else
		{
			for (j = l, j < m + 1, j++)
				sum += nums[j];
			avg = sum / (m - l + i);
			avg = floor(avg);
			avgs[i] = avg;
		}
	}
	return (avgs);
}
