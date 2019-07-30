from __future__ import division
from math import ceil

T = int(raw_input())
for t in xrange(T):
	C, F, X = map(float, raw_input().split())
	rate = 2
	time = 0

	while True:
		time_to_win = X / rate
		time_to_farm_then_win = C / rate + X / (F + rate)
		if time_to_win <= time_to_farm_then_win:
			time += time_to_win
			break
		else:
			time += C / rate
			rate += F

	# rate_needed = F * (X - C) / C
	# num_farms_needed = ceil((rate_needed - 2) / F)
	# if num_farms_needed < 0: num_farms_needed = 0
	# actual_rate = num_farms_needed * F + 2
	# time_to_buy_farms = num_farms_needed * (actual_rate + 2) / 2
	# time_to_win = time_to_buy_farms + X / actual_rate
	# print time_to_buy_farms

	print "Case #%d: %.7f" % (t + 1, time)
