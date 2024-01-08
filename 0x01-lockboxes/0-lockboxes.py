#!/usr/bin/python3
"""doc"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    opened_boxes = [0]
    index = 0

    while index < len(opened_boxes):
        current_box = opened_boxes[index]

        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.append(key)

        index += 1

    return len(opened_boxes) == len(boxes)
