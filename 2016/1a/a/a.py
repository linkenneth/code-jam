#!/usr/bin/local/python

import collections

def computeLongestPath(student, origin):
    print(student, origin, longestPathLength)

    if student == origin:
        # indicate that this is a cycle. Also, the current node does not count
        # towards the path length
        return -1
    elif not inboundEdges.get(student):
        return 0
    elif student in longestPathLength:
        return longestPathLength[student]

    currentLength = 0
    for otherStudent in inboundEdges[student]:
        # print(student, otherStudent, studentsWhoLikeStudent)
        length = computeLongestPath(otherStudent, origin)
        if length == -1:
            # this is a cycle. set path length of everything on this path to
            # said length.
        if length > currentLength:
            currentLength = length

    # longestPathLength[student] = max(
    #     computeLongestPath(otherStudent, origin) + 1
    #     for otherStudent in inboundEdges[student])
    return longestPathLength[student]

T = int(input())
for t in range(T):
    N = int(input())
    bffList = [int(f) for f in input().split()]

    # record both inbound and outbound edges
    outboundEdges = {}
    inboundEdges = collections.defaultdict(lambda: [])

    for i, bff in enumerate(bffList):
        student = i + 1
        outboundEdges[student] = bff
        inboundEdges[bff].append(student)

    print('Outbound Edges: ', outboundEdges)
    print('Inbound Edges: ', inboundEdges)

    # longest path length with `key` as destination
    longestPathLength = {}
    for student, studentsWhoLikeStudent in inboundEdges.items():
        longestPathLength[student] = max(
            computeLongestPath(otherStudent, student) + 1
            for otherStudent in studentsWhoLikeStudent)
        print(' -- longest path for {}: {}'.format(
            student, longestPathLength[student]))

    print('Longest path length: ', longestPathLength)
