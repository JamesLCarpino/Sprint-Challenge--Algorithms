class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l  # The list the robot is tasked with sorting
        self._item = None  # The item the robot is holding
        self._position = 0  # The list position the robot is at
        self._light = "OFF"  # The state of the robot's light
        self._time = 0  # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # Bubble sort I beleive would be best utilized here no?
        # reasoning: I need this robot to compare items left and right and swap as it goes.
        # might eat up a crap ton of runtime but should work eventually...ehh maybe not

        # psuedo code and james thoughts:

        # the robot may pick up one item at a time or else it swaps what it has -> useful:
        # because if the robot is picking up and dropping each of the items it is currently holding
        # it can start at [0] pick up an item
        # , check to see if it can move right
        # , if it can than it will check the next index value
        # if the current item is > the index value being evaluated it will check to see if it can move right
        # if it can it will move right and repeat.
        # if it cannot move right it will drop that item in that position
        # if the current item is < the index value being evaluated it will swap the numbers
        # now it is holding the greater number than the index so it can move to the right.
        # repeat steps...eventually this will get the largest number to the end of the array.
        # at the end of the array it won't be able to move right.
        # if check_right ==  start over again. recusion --> or would be cool to do the opposite at the end of the array moving left.
        # if it cannot move right that means it can move left:
        # this means its at the end of the array.
        # if at len(arr)-1 then it cannot move right because there is no more room
        # check if it can move left.

        # so pick up item to the left of the last item.

        # general rules
        # pick up whatever that item is,
        # compare if it is greater than or less than,
        # if it is greater than the number it is currently holding move to the right
        # if it is less than the number it is currently holding swap it
        #
        # -------------------------------------------------------------------------------#
        # base case l is empty:
        if self._list == 0:
            return l

        # moving left? at any point do I need to move left? If i'm just going to recursively check this thing?


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`
    l = [5, 7, 9, 2, 1]
    # l = [
    #     15,
    #     41,
    #     58,
    #     49,
    #     26,
    #     4,
    #     28,
    #     8,
    #     61,
    #     60,
    #     65,
    #     21,
    #     78,
    #     14,
    #     35,
    #     90,
    #     54,
    #     5,
    #     0,
    #     87,
    #     82,
    #     96,
    #     43,
    #     92,
    #     62,
    #     97,
    #     69,
    #     94,
    #     99,
    #     93,
    #     76,
    #     47,
    #     2,
    #     88,
    #     51,
    #     40,
    #     95,
    #     6,
    #     23,
    #     81,
    #     30,
    #     19,
    #     25,
    #     91,
    #     18,
    #     68,
    #     71,
    #     9,
    #     66,
    #     1,
    #     45,
    #     33,
    #     3,
    #     72,
    #     16,
    #     85,
    #     27,
    #     59,
    #     64,
    #     39,
    #     32,
    #     24,
    #     38,
    #     84,
    #     44,
    #     80,
    #     11,
    #     73,
    #     42,
    #     20,
    #     10,
    #     29,
    #     22,
    #     98,
    #     17,
    #     48,
    #     52,
    #     67,
    #     53,
    #     74,
    #     77,
    #     37,
    #     63,
    #     31,
    #     7,
    #     75,
    #     36,
    #     89,
    #     70,
    #     34,
    #     79,
    #     83,
    #     13,
    #     57,
    #     86,
    #     12,
    #     56,
    #     50,
    #     55,
    #     46,
    # ]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
