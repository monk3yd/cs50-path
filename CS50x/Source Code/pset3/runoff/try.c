
    int find_min(void)
{
    //iterate through candidates[].votes array. search for smaller number of votes.
    int c = voter_count;
    
    for (int i = 0; i < candidate_count; i++) //iterate through eliminated array for discarding true candidates.
    {
        if (candidates[i].eliminated == false)
        {
            for (int j = 0; j < candidate_count; j++)
            {
                if (c > candidates[j].votes)
                {
                    c = candidates[j].votes;
                }
            }
            return c;
        }
    }
    return 0;
}






 for (int i = 0; i < candidate_count; i++) // TODO
    {
        if (candidates[i].eliminated == false)
        {
            if(candidates[i].votes == min)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
    }
    return false;