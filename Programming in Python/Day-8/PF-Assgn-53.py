#PF-Assgn-53
#This verification is based on string match.
import re

poem='''
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

pattern = re.compile(r"v")
matches=pattern.finditer(poem)
count=0
for match in matches:
    count=count+1
print(count)
print(re.sub(r'(\n+)(?=[A-Z])', r' ', poem))

