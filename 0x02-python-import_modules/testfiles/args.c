#include <stdio.h>

/**
 * main - Main Entry
 * @argc : arguments count
 * @argv : arguments vector
 * Return: 0
 */
int main(int argc, char *argv[])
{
	int i;

	if (argc < 2)
	{
		printf("0 arguments.\n");
	}
	else
	{
		printf("%d arguments:\n", argc - 1);
	}

	for (i = 1; i < argc; i++)
	{
		printf("%d: %s\n", i, argv[i]);
	}

	return (0);
}
