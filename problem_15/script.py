#!env/bin/python

import sys,math
import helpers as zfunc
import structures as zstruct


def solve_path(latt, end):
    if latt.get_value() == 1:
        return 0
    else:
        latt.set_value(1)
    if (latt.get_pos()["x"] == end["x"]) and (latt.get_pos()["y"] == end["y"]):
#        print "Solution:"
#        latt.print_grid()
        return 1
    else:
        result = 0
        neighbors = latt.get_neighbors()
        for nb in neighbors:
            if (nb["x"] > latt.get_pos()["x"]) or (nb["y"] > latt.get_pos()["y"]):
                cp = latt.get_pos()
                latt.set_pos(nb["x"],nb["y"])
                result += solve_path(latt, end)
                latt.set_value(0)
                latt.set_pos(cp["x"],cp["y"])
        return result
                
num=21
#lt = zstruct.Lattice(num,num)
#print "Total:"
#print solve_path(lt, {"x" : num-1, "y" : num-1})
print zfunc.n_choose_r(40,20)

