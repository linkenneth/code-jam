import numpy as np
import copy

T = int(raw_input())
for t in xrange(T):
	N = int(raw_input())
	naomi = map(float, raw_input().split())
	ken = map(float, raw_input().split())

	naomi.sort()
	ken.sort()

	# print naomi
	# print ken

	ken_war = copy.copy(ken)

	# calculate war score
	war_score = 0
	for chosen_naomi in naomi:
		index = np.searchsorted(ken_war, chosen_naomi)
		if index >= len(ken_war):
			war_score += 1
			# print chosen_naomi, ken_war[0], 'score'
			ken_war.pop(0)
		else:
			# print chosen_naomi, ken_war[index]
			ken_war.pop(index)

	# calculate deceitful war score
	# print naomi
	# print ken
	deceitful_score = 0
	for i in xrange(N):
		naomi_deceit = np.array(naomi[i:])
		ken_deceit = np.array(ken[:N-i])
		deceitful_score = max(deceitful_score, (naomi_deceit > ken_deceit).sum())

	print 'Case #%d: %d %d' % (t + 1, deceitful_score, war_score)
