#!env/bin/python

t = 400
rt = 0
r = [[]]
for p200 in range(0,2):
    rt = 0
    t200 = p200*200
    if rt + t200 == t:
        r.append([0,0,0,0,0,0,0,p200])
        continue
    elif rt+t200 > t:
        break
    else:
        rt += t200
        for p100 in range(0,(t)/100+1):
            t100 = p100*100
            if rt + t100 == t:
                r.append([0,0,0,0,0,0,p100,p200])
                continue
            elif rt+t100 > t:
                break
            else:
                rt += t100
                for p50 in range(0,(t)/50+1):
                    t50 = p50*50
                    if rt + t50 == t:
                        r.append([0,0,0,0,0,p50,p100,p200])
                        continue
                    elif rt+t50 > t:
                        break
                    else:
                        rt += t50
                        for p20 in range(0,(t)/20+1):
                            t20 = p20*20
                            if rt + t20 == t:
                                r.append([0,0,0,0,p20,p50,p100,p200])
                                continue
                            elif rt+t20 > t:
                                break
                            else:
                                rt += t20
                                for p10 in range(0,(t)/10+1):
                                    t10 = p10*10
                                    if rt + t10 == t:
                                        r.append([0,0,0,p10,p20,p50,p100,p200])
                                        continue
                                    elif rt+t10 > t:
                                        break
                                    else:
                                        rt += t10
                                        for p5 in range(0,(t)/5+1):
                                            t5 = p5*5
                                            if rt + t5 == t:
                                                r.append([0,0,p5,p10,p20,p50,p100,p200])
                                                continue
                                            elif rt + t5 > t:
                                                break
                                            else:
                                                rt += t5
                                                for p2 in range(0,(t)/2+1):
                                                    t2 = p2*2
                                                    if rt + t2 == t:
                                                        r.append([0,p2,p5,p10,p20,p50,p100,p200])
                                                        continue
                                                    elif rt + t2 > t:
                                                        break
                                                    else:
                                                        rt += t2
                                                        for p1 in range(0,t+1):
                                                            t1 = p1
                                                            if rt + t1 == t:
                                                                r.append([p1,p2,p5,p10,p20,p50,p100,p200])
                                                                continue
                                                            elif rt + t1 > t:
                                                                break
                                                        rt -= t2
                                                rt -= t5
                                        rt -= t10
                                rt -= t20
                        rt -= t50
                rt -= t100
        rt -= t200

print len(r)
