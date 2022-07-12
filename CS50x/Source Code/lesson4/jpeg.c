//check if a file, passed it's name in the command line, is a JPEG or not.

#include <stdio.h>

int main(int argc, char *argv[])
{
    //ensue user ran program with two words at prompt.
    if (argc != 2)
    {
        return 1;
    }

    //open file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        return 1;
    }

    //read the first 3 bytes (24 bits) from the file
    unsigned char bytes[3];
    fread(bytes, 3, 1, file);

    //check first three bytes. if bytes are 0xff 0xd8 0xff
    if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff)
    {
        printf("Maybe\n");
    }
    else
    {
        printf("No\n");
    }

    //close file
    fclose(file);
}