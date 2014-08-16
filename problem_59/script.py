#!env/bin/python

def decode(cipher_codes, password):
    result = []
    plen = len(password)
    clen = len(cipher_codes)
    cpos = 0
    char_list = ['@', '#', '$', '%', '^', '&', '*']
    while cpos < clen:
        ppos = 0
        while ppos < plen and cpos + ppos < clen:
            char = cipher_codes[cpos + ppos]
            dchar = chr(int(char) ^ ord(password[ppos]))
            if dchar in char_list:
                return ['!']
            else:
                result.append(dchar)
            ppos += 1
        cpos += plen
    return result

def main():
    word_list = ['the', 'be', 'to', 'of', 'and', 'that', 'have', 'for', 'not']

    __f = open('cipher1.txt','r')

    cipher1 = __f.read()
    cipher_codes = cipher1.split(',')
    cipher_text = []

    for c1 in xrange(ord('a'), ord('z')+1):
        for c2 in xrange(ord('a'), ord('z')+1):
            for c3 in xrange(ord('a'), ord('z')+1):
                deciphered_chars = decode(cipher_codes, \
                    "{}{}{}".format(chr(c1),chr(c2),chr(c3)))
                deciphered_text = ''.join(deciphered_chars)
                word_count = 0
                for word in word_list:
                    if deciphered_text.find(word) >= 0:
                        word_count += 1
                if word_count > 7:
                    print (deciphered_text)
                    __r = [ ord(c) for c in deciphered_text ]
                    print sum(__r)
                    return 0

if __name__ == '__main__':
    main()
