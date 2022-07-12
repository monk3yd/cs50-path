#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string names[4];
    names[0] = "EMMA";
    names[1] = "RODRIGO";
    names[2] = "BRIAN";
    names[3] = "DAVID";

    printf("%s\n", names[0]);

//I know emma's name is a string, and that a string is an array of characters. so:
//you can create what's essentially a two dimensional array, you have two sets of []
//the first one indexes me into array names ("go to a certain location in an array"). in this case the first [0] means go get emma's name from the array of four names.
//the second one says within that string treat it as an array of characters and get [n] character or emma's name.

    printf("%c%c%c%c%i\n", names[0][0], names[0][1], names[0][2], names[0][3], names[0][4]);
                                                // names[0][400] we can actually start hacking and looking around computer's memory at any location, because it's just numbers of boxes on the screen

    //This is just ridiculous, but is equivalent to printing the string iself. it also prints the null character.
}