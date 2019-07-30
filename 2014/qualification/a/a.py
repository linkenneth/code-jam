T = int(raw_input())
for t in xrange(T):
	r1 = int(raw_input())
	cards = [ map(int, raw_input().split()) for _ in xrange(4) ]
	pr1 = set(cards[r1 - 1])
	r2 = int(raw_input())
	cards = [ map(int, raw_input().split()) for _ in xrange(4) ]
	pr2 = set(cards[r2 - 1])
	s = list(pr1 & pr2)
	if len(s) == 1:
		print "Case #%d: %d" % (t + 1, s[0])
	elif len(s) > 1:
		print "Case #%d: Bad magician!" % (t + 1)
	else:
		print "Case #%d: Volunteer cheated!" % (t + 1)
