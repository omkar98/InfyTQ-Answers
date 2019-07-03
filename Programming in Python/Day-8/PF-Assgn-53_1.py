#PF-Assgn-53
#This verification is based on string match.
import re

poem='''
It takes strength for being certain,
It takes courage to have doubt.
It takes strength for challenging alone,
It takes courage to lean on another.
It takes strength for loving other souls,
It takes courage to be loved.
It takes strength for hiding our own pain,
It takes courage to help if it is paining for someone.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

pattern = re.compile(r"v")
matches=pattern.finditer(poem)
count=0
for match in matches:
    count=count+1
print(count)

print("\n"+re.sub(r'(\n+)(?=[A-Z])', r' ', poem))
print(re.sub(r"co",r"Co",re.sub(r"ch",r"Ch",poem)))
print(re.sub(r"hi...",r"hi*/*",re.sub(r"ai...",r"ai*/*",poem)))
