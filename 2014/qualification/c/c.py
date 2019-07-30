from __future__ import division
from math import ceil

def print_grid(R, C, M):
	grid = [['*'] * C for r in xrange(R) ]
	to_clear = R * C - M

	rp, cp = 0, 0
	while to_clear > 0:
		r_ = min(rp, R - 1)
		c_ = min(cp, C - 1)
		if rp < R:
			# print "R clear %d" % rp
			# print rp, cp
			for i in xrange(c_ + 1):
				grid[r_][i] = '.'
				to_clear -= 1
				if to_clear == 0: break
			# for row in grid:
			# 	print ''.join(row)
		if to_clear == 0: break
		cp += 1
		c_ += 1
		if cp < C:
			# print "C clear %d" % cp
			# print rp, cp
			for j in xrange(r_ + 1):
				grid[j][c_] = '.'
				to_clear -= 1
				if to_clear == 0: break
			# for row in grid:
			# 	print ''.join(row)
		rp += 1
		r_ += 1

	grid[0][0] = 'c'

	return grid

T = int(raw_input())
for t in xrange(T):
	R, C, M = map(int, raw_input().split())

	print "Case #%d:" % (t + 1)
	if M == 0:
		grid = print_grid(R, C, M)
	elif R == 1:
		if C - M < 2:
			print "Impossible"
			continue
		else:
			grid = print_grid(R, C, M)
	elif C == 1:
		if R - M < 2:
			print "Impossible"
			continue
		else:
			grid = print_grid(R, C, M)
	else:
		if R * C - M < 4:
			print "Impossible"
			continue
		else:
			grid = print_grid(R, C, M)

	for row in grid:
		print ''.join(row)
