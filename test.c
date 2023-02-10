#include <stdio.h>

void main() {
	FILE *file;
	char line[26];
	file = fopen("/home/lerskk/code/python/practice6/cp.txt", "w+");
	printf("%d", ftell(file));
	fprintf(file, "my name is file \n lol");
	printf("%d", ftell(file));
	fseek(file, 100, SEEK_SET);
	printf("%d", ftell(file));
	fprintf(file, "my name is file \n lol");
	printf("%d", ftell(file));
	fscanf(file, "%[^\n]", line);
	printf("%d", ftell(file));
	printf("%s", line);
	fclose(file);
}