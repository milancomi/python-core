import re

patterns = ['term1','term2']

text = 'This is a string with term1, not not the oher!'




# for pattern in patterns:
#     print("I'am searching for: "+pattern)
#     if re.search(pattern,text):
#         print("MATCH!")

#     else:
#         print("NO MATCH!")


match = re.search('term1',text)

print(match.start()) # term krece od indexa broj 22


split_term ='@'
email = 'user@gmail.com'
print(re.split(split_term,email))



print(re.findall('match','test phrase match in middle'))

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')


test_phrase = 'ssd.sssddd.sdddsddd...dsd.dsssss...sdddd'

test_patterns = ['sd*'] # s sa 0 or more D
test_patterns2 = ['sd+'] # s sa 1 or more D
test_patterns3 = ['sd?'] # s sa 0 or 1 D
test_patterns4 = ['sd{3}'] # s sa 3 D
test_patterns5 = ['sd{2,3}'] # s sa 2 or 3 D

test_pattenrs6 =['s[sd]+'] # s sa S or D 1 or more

multi_re_find(test_patterns,test_phrase)


# exklusion

test_phrase2 = 'This is a string! But is has punctuation. How can we remove it? 123123123'
test_patterns7 =['[^!.?]+'] # exclude

test_patterns8 =['[a-z]+']
test_patterns9 =['[A-Z]+']

test_patterns10 = [r'\d+'] # digits
test_patterns11 = [r'\D+'] # NONDIGITS
test_patterns12 = [r'\s+'] # whitespace
test_patterns13 = [r'\D+'] # nonwhitespace
test_patterns14 = [r'\w+'] # alfanumeric
test_patterns15 = [r'\W+']  #nonalfanumeric
