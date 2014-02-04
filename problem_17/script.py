#!env/bin/python


def word_conv(n):
    ns = str(n)
    nl = len(ns)
    nr = ns[::-1]
    pos = 0
    result = ''
    for c in nr:
        if pos == 0:
            if c == '1':
                result = 'one'
            elif c == '2':
                result = 'two'
            elif c == '3':
                result = 'three'
            elif c == '4':
                result = 'four'
            elif c == '5':
                result = 'five'
            elif c == '6':
                result = 'six'
            elif c == '7':
                result = 'seven'
            elif c == '8':
                result = 'eight'
            elif c == '9':
                result = 'nine'
        elif pos == 1 and c == '1':
            c1 = nr[0:2][::-1]
            if c1 == '10':
                result = "ten"
            elif c1 == '11':
                result = "eleven"
            elif c1 == '12':
                result = "twelve"
            elif c1 == '13':
                result = "thirteen"
            elif c1 == '14':
                result = "fourteen"
            elif c1 == '15':
                result = "fifteen"
            elif c1 == "16":
                result = "sixteen"
            elif c1 == "17":
                result = "seventeen"
            elif c1 == "18":
                result = "eighteen"
            elif c1 == "19":
                result = "nineteen"
        elif pos == 1:
            if c == "2":
                if len(result) > 0:
                    result = 'twenty-'+result
                else:
                    result = 'twenty'
            elif c == "3":
                if len(result) > 0:
                    result = 'thirty-'+result
                else:
                    result = 'thirty'
            elif c == "4":
                if len(result) > 0:
                    result = 'forty-'+result
                else:
                    result = 'forty'
            elif c == "5":
                if len(result) > 0:
                    result = 'fifty-'+result
                else:
                    result = 'fifty'
            elif c == "6":
                if len(result) > 0:
                    result = 'sixty-'+result
                else:
                    result = 'sixty'
            elif c == "7":
                if len(result) > 0:
                    result = 'seventy-'+result
                else:
                    result = 'seventy'
            elif c == "8":
                if len(result) > 0:
                    result = 'eighty-'+result
                else:
                    result = 'eighty'
            elif c == "9":
                if len(result) > 0:
                    result = 'ninety-'+result
                else:
                    result = 'ninety'
        elif pos == 2:
            if c == "1":
                if len(result) > 0:
                    result = "one hundred and "+result
                else:
                    result = "one hundred"
            elif c == "2":
                if len(result) > 0:
                    result = "two hundred and "+result
                else:
                    result = "two hundred"
            elif c == "3":
                if len(result) > 0:
                    result = "three hundred and "+result
                else:
                    result = "three hundred"
            elif c == "4":
                if len(result) > 0:
                    result = "four hundred and "+result
                else:
                    result = "four hundred"
            elif c == "5":
                if len(result) > 0:
                    result = "five hundred and "+result
                else:
                    result = "five hundred"
            elif c == "6":
                if len(result) > 0:
                    result = "six hundred and "+result
                else:
                    result = "six hundred"
            elif c == "7":
                if len(result) > 0:
                    result = "seven hundred and "+result
                else:
                    result = "seven hundred"
            elif c == "8":
                if len(result) > 0:
                    result = "eight hundred and "+result
                else:
                    result = "eight hundred"
            elif c == "9":
                if len(result) > 0:
                    result = "nine hundred and "+result
                else:
                    result = "nine hundred"
        elif pos == 3:
            result = "one thousand"
        pos += 1
    return result

result = ''
for x in range(1,1001,1):
    result += word_conv(x).replace(' ','').replace('-','')

print result
print len(result)
print (word_conv(342).replace(' ','').replace('-',''))
