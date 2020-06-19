#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

b) O(n^2) -> the bigger n gets the more opperations occure meaning in this case that as it is looping the number of operations will increase squarely. Therefor longer. Specifically in this case it is running the first loop n times and then the second loop n times ie: n^2.

c)

## Exercise II

n is the amount of stories in the building
f is the height at which eggs begin to die
anything < f will be okay, anything >= f will die
n being the story at which f is so when n == f -> thats the first point at which eggs will die:
if n >= f is a broken egg
if n < f will be okay and remain unscrambled.

I'd probably use a binary search to eliminate large portions of the code and hone in on the f. This would minimize the amount of eggs lost because if you were to drop one egg at the mid point of len(n) and it didn't break you could eliminate everything to the left of that, and then move up until the first broken egg and then eliminate everything to the right after that giving you the f of when those eggs begin to meet their demise, and reverse it if it were the other way around. This would be a run time of O(n) because its doing O(1) per node.
