#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)  // TODO
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    //printf("%s\n", candidates[candidate_count - 2].name);
    //printf("%i\n", candidates[candidate_count - 2].votes);

    candidate tmp;
    for (int i = 0; i < candidate_count - 1; i++)       //bubble sort arrays in struct
    {
        for (int j = 0; j < candidate_count - i - 1; j++)
        {
            if (candidates[j].votes > candidates[j + 1].votes)
            {
                tmp = candidates[j];

                candidates[j] = candidates[j + 1];

                candidates[j + 1] = tmp;
            }
        }
    }

//search for biggest number of votes
    int c = 0;
    for (int k = 0; k < candidate_count; k++)
    {
        if (candidates[k].votes > c)
        {
            c = candidates[k].votes;
        }
    }

//search and print all candidates with most number of votes
    for (int l = 0; l < candidate_count; l++)
    {
        if (candidates[l].votes == c)
        {
            printf("%s\n", candidates[l].name);
        }
    }

    //printf("%s\n", candidates[candidate_count - 1].name);
    //printf("%i\n", candidates[candidate_count - 1].votes);
    //printf("%i\n", c);
    return;
}