//declaration
bool valid_triangle(float x, float y, float z);

//definition
bool valid_triangle(float x, float y, float z)
{
    // chech all positive sides
    if (x <= 0 || y <=0 || z <= 0)
    {
        return false;
    }

    //check that sum of any two sides is greater than third
    if (x + y <= z || x + z <= y || y + z <= x)
    {
        return false;
    }

    //if we passed both tests, we're good!
    return true;
}