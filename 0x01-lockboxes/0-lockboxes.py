#!/usr/bin/python3
"""
Module for lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Args:
        boxes (list): A list of lists where each inner list represents a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = set([0])
    visited = set()

    while keys:
        current_key = keys.pop()

        if current_key in visited:
            continue

        visited.add(current_key)

        for key in boxes[current_key]:
            if key not in visited and key < len(boxes):
                keys.add(key)

    return len(visited) == len(boxes)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
