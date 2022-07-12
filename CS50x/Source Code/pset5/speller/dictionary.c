// Implements a dictionary's functionality
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 47000;

// Hash table
node *table[N];

//global variables
unsigned int wcounter = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    //hash word to obtain hash value
    unsigned int x = hash(word);

    //access llist at that index in hash table
    node *cursor = table[x];

    //trav llist, looking for word (strcasecmp)
    while(cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) != 0)
        {
            cursor = cursor->next;
        }
        else
        {
            return true;
        }
    }
    return false;
}

//Hashes word to a number.
//Modified djb2 hash function from http://www.cse.yorku.ca/~oz/hash.html      thanks ;)
unsigned int hash(const char *word)
{
    unsigned int hash = 5381;
    int c;

    while ((c = *word++))
        hash = ((hash << 5) + hash) + tolower(c);    /* hash * 33 + c */

    return hash % N;
}

// Loads dictionary into memory, returning true if successful else false.
bool load(const char *dictionary)
{
    char word[LENGTH + 1];

    //open dictionary file.
    FILE *dfile = fopen(dictionary, "r");
    if (dfile  == NULL)
    {
        return false;
    }

    //read strings from file one at a time until EOF
    while (fscanf(dfile, "%s", word) != EOF)
    {
        //create a new node(n) for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }

        //copy word into new node
        strcpy(n->word, word);

        //set new node pointer to NULL
        n->next = NULL;

        //hash word to obtain hash value
        unsigned int x = hash(word);

        //insert node into hash table at that location
        if(table[x] == NULL)
        {
            table[x] = n;
        }
        else
        {
            n->next = table[x]->next;
            table[x]->next = n;
        }
        wcounter++;
    }

    fclose(dfile);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (wcounter != 0)
    {
        return wcounter;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N - 1; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
            if (cursor == NULL)
            {
                free(cursor);
            }
        }
    }
    return true;
}
