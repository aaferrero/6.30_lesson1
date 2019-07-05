import jieba
import random
def is_variable(pat):
    return pat.startswith('?') and all(s.isalpha() for s in pat[1:])
def pat_match(pattern, saying):
    if is_variable(pattern[0]): return True
    else:
        if pattern[0] != saying[0]: return False
        else:
            return pat_match(pattern[1:], saying[1:])

#print(pat_match('I want ?X'.split(), "I want holiday".split()))
str1='I want ?X'.split()
#print(str1[0].startswith('?'))
#print(is_variable('I want ?X'.split()[0]))
##print(str1[])
print(all(s.isalpha() for s in '11111'))

def pat_match(pattern, saying):
    if is_variable(pattern[0]):
        return pattern[0], saying[0]
    else:
        if pattern[0] != saying[0]: return False
        else:
            return pat_match(pattern[1:], saying[1:])

pattern = 'I want ?X'.split()
saying = "I want holiday".split()
pattern ='?我 equals ?X'.split()
saying ='2+2 equals 2+23'.split()

print(pat_match(pattern, saying))


def pat_match(pattern, saying):
    if not pattern or not saying: return []

    if is_variable(pattern[0]):
        return [(pattern[0], saying[0])] + pat_match(pattern[1:], saying[1:])
    else:
        if pattern[0] != saying[0]:
            return []
        else:
            return pat_match(pattern[1:], saying[1:])
print(pat_match("?X greater than ?Y".split(), "3 greater than 2".split()))

def pat_to_dict(patterns):
    return {k: v for k, v in patterns}

def subsitite(rule, parsed_rules):
    if not rule: return []
    return [parsed_rules.get(rule[0], rule[0])] + subsitite(rule[1:], parsed_rules)

got_patterns = pat_match("?p want ?X".split(), "I want iPhone".split())
sub=subsitite("What if you mean if ?p got a ?X".split(), pat_to_dict(got_patterns))
print(sub)

def is_pattern_segment(pattern):
    return pattern.startswith('?*') and all(a.isalpha() for a in pattern[2:])

from collections import defaultdict

fail = [True, None]


def pat_match_with_seg(pattern, saying):
    if not pattern or not saying: return []

    pat = pattern[0]

    if is_variable(pat):
        return [(pat, saying[0])] + pat_match_with_seg(pattern[1:], saying[1:])
    elif is_pattern_segment(pat):
        match, index = segment_match(pattern, saying)
        return [match] + pat_match_with_seg(pattern[1:], saying[index:])
    elif pat == saying[0]:
        return pat_match_with_seg(pattern[1:], saying[1:])
    else:
        return fail


def segment_match(pattern, saying):
    seg_pat, rest = pattern[0], pattern[1:]
    seg_pat = seg_pat.replace('?*', '?')

    if not rest: return (seg_pat, saying), len(saying)

    for i, token in enumerate(saying):
        if rest[0] == token and is_match(rest[1:], saying[(i + 1):]):
            return (seg_pat, saying[:i]), i

    return (seg_pat, saying), len(saying)


def is_match(rest, saying):
    if not rest and not saying:
        return True
    if not all(a.isalpha() for a in rest[0]):
        return True
    if rest[0] != saying[0]:
        return False
    return is_match(rest[1:], saying[1:])

def pat_to_dict(patterns):
    return {k: ' '.join(v) if isinstance(v, list) else v for k, v in patterns}

print(pat_match_with_seg('?*P is very good and ?*X'.split(), "My dog is very good and my cat is very cute".split()))

print(pat_match_with_seg('I need ?*X'.split(), "I neead an iPhone".split()))

print(subsitite("Why do you need ?X".split(), pat_to_dict(pat_match_with_seg('I need ?*X'.split(),
                  "I need an iPhone".split()))))
print(subsitite("Hi, how do you do?".split(), pat_to_dict(pat_match_with_seg('?*X hello ?*Y'.split(),
                  "hello".split()))))
######################################################################
##########################################################################
######################################################################

def get_response(saying, response_rules):
    print('answer:')
    print(' '.join(subsitite(random.choice(list(response_rules.values())[0]).split(), pat_to_dict(pat_match_with_seg(list(rules.keys())[0].split(),
                  saying.split())))).replace(' ',''))

rules = {
    "insurance age is ?*Y": ["what is insurance age?",'?Y is your insurance age?']
}
saying="insurance age is 18 years old"

#print(list(rules.keys()))
#########################################################################
####PROBLEM 2 and 3
for number in range(10):
    print('ask:\n',saying)
    get_response(saying,rules)

rules = {
    ' '.join(jieba.cut("投保年龄是"))+' ?*Y': [' '.join(jieba.cut("什么是投保年龄?")),'?Y '+' '.join(jieba.cut('是你的投保年龄?'))]
}
saying=' '.join(jieba.cut('投保年龄是18周岁'))
for number in range(10):
    print('ask:\n',saying.replace(' ',''))
    get_response(saying,rules)