//goal to write a phonebook program that lets me type in a human's name and number and just keep appending it to a text file.
//like a database that i can store if i want to keep track of people's phone numbers.

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    //open file
    FILE *file = fopen("phonebook.csv", "a"); //give me a pointer to a FILE and call it lower case file.//"a" append or "w" write or "r" read

    //get strings from user
    char *name = get_string("Name: ");
    char *number = get_string("Number: ");

    //print (write) strings to file
    fprintf(file, "%s, %s\n", name, number);

    //close file
    fclose(file);
}