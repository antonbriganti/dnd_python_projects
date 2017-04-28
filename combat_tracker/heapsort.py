__author__ = 'Anton Briganti'
from heapq import *


def initiative():
    combat_number = int(input("How many in combat? "))
    initiative_heap = []

    for i in range(combat_number):
        mon_type = input("Type: ")
        name = input("Name: ")
        init = int(input("Initiative: "))
        print()
        heappush(initiative_heap, (init*-1, [name, mon_type]))

    for i in range(len(initiative_heap)):
        initiative_heap[i] = [initiative_heap[i][0] * -1, initiative_heap[i][1][0], initiative_heap[i][1][1]]

    return initiative_heap

initiative()
