import pstats, cProfile
import script

cProfile.runctx("script.main()", globals(), locals(), "Profile.prof")
s = pstats.Stats("Profile.prof")
print "Stats:"
print s
s.strip_dirs().sort_stats("time").print_stats()
