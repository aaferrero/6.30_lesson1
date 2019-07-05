import random
import sys
def adj():
    return random.choice(['蓝色的 ', ' 好看的 ', ' 小小的']).split()[0]


def adj_star():
    return random.choice([lambda : '', lambda : adj() + adj_star()])()

#print(adj())
#print('蓝色的 | 好看的 | 小小的'.split('|'))
for number in range(20):
    print(adj_star())
print('-----------------------------------------')
def aa():
    return random.choice([lambda:2,(lambda:(aa()+1))])()
#for number in range(20):
    #print(aa())

adj_grammar ="""
Adj* => null | Adj Adj*
Adj =>  蓝色的 | 好看的 | 小小的
"""

simple_grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article =>  一个 | 这个
noun =>   女人 |  篮球 | 桌子 | 小猫
verb => 看着   |  坐在 |  听着 | 看见
Adj =>  蓝色的 | 好看的 | 小小的
"""
def create_grammar(grammar_str, split='=>', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip():
            continue
        exp, stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
        #print(grammar[exp.strip()])
    return grammar


print(create_grammar(simple_grammar))
print('------------------------------------------------------')
example_grammar = create_grammar(simple_grammar)
choice = random.choice


def generate(gram, target):
    if target not in gram:
        return target  # means target is a terminal expression
    choice1=choice(gram[target])

    expaned = [generate(gram, t) for t in choice(gram[target])]
    #print(111,expaned)
    return ''.join([e if e != '/n' else '\n' for e in expaned if e != 'null'])

#for number in range(20):
    #print(generate(gram=example_grammar, target='sentence'))
#print( choice(example_grammar['sentence']))

#code_achieve-1
#westworld huamn language

######################################################################################
######################################################################################
######################################################################################
######################################################################################
###asignment!!!!!
west_huaman_grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article =>  一个 | 这个
noun =>   女人 |  篮球 | 桌子 | 小猫
verb => 看着   |  坐在 |  听着 | 看见
Adj =>  蓝色的 | 好看的 | 小小的
"""

west_huaman_grammar = """
human => body feek activity
body => null | body1
body1 => 我 | 俺 | 我们
feek => 看看 | 找找 | 想找点
activity => 乐子 | 玩的
"""
west_huaman_grammar=create_grammar(west_huaman_grammar)

for number in range(20):
    print(generate(gram=west_huaman_grammar, target='human'))
print('------------------------------------------------------')

host = """
host == 寒暄 host_报数 
host_报数== numberoff_inquire_business_related_end1 | inquire_business_related_end_numberoff
numberoff_inquire_business_related_end1== 报数 询问 业务相关 结尾
inquire_business_related_end_numberoff== 询问 业务相关 结尾 报数
报数 == 我是 数字 号 ,
数字 == 单个数字 | 数字 单个数字 
单个数字 == 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 == 称谓 打招呼 | 打招呼
称谓 == 人称 ,
人称== 先生 | 女士 | 小朋友
打招呼 == 你好 | 您好 
询问 == 请问你要 | 您需要
业务相关 == 玩玩 具体业务
玩玩 == null
具体业务 == 喝酒 | 打牌 | 打猎 | 赌博
结尾 == 吗？
"""
host_grammar=create_grammar(host,split='==')

for number in range(30):
    print(generate(gram=host_grammar, target='host'))
print('------------------------------------------------------')

import re
from functools import reduce
def token(string):
    # we will learn the regular expression next course.
    regex_str = ".*?([0-9\u4E00-\u9FA5]+)"
    return re.findall(regex_str, string)

#words = ['study in 山海大学吾问无为谓','问问非常']
#print(token(words))

import jieba

def cut(string):
    return list(jieba.cut(string))

with open('train.txt',encoding='utf-8') as r:               #train.txt文件在当面目录
    text_line=r.readlines()
    #text_line_jieba=[]
    TOKEN=[]
    for i, line in enumerate(text_line):
        #if i % 100 == 0: print(i)

        # replace 10000 with a big number when you do your homework.
        #print(token(line))

        if len(token(line))>2:
            #print(token(line))
            lines=reduce(lambda x,y:x+y,token(line)[1:])
            #print(lines)
            TOKEN += cut(lines)

            #print(lines)
        elif len(token(line))==2:
            TOKEN += cut(token(line)[1])
        #assert len(token(line))==2
        #print(TOKEN)

        #if i > 20000:
            #break

        #print(cut(token(line)[0]))
from collections import Counter
words_count = Counter(TOKEN)
print(words_count.most_common(100))
TOKEN = [str(t) for t in TOKEN]
print(TOKEN)
TOKEN_2_GRAM = [''.join(TOKEN[i:i+2]) for i in range(len(TOKEN[:-2]))]
print(TOKEN_2_GRAM[:10])
words_count_2 = Counter(TOKEN_2_GRAM)
def prob_2(word1, word2):
    if word1 + word2 in words_count_2:
        print('{d} in models!'.format(d=word1 + word2))
        return words_count_2[word1+word2] / len(TOKEN_2_GRAM)
    else:
        return 1 / len(TOKEN_2_GRAM)
print(prob_2('保险', '年龄'))


def get_probablity(sentence):
    words = cut(sentence)

    sentence_pro = 1

    for i, word in enumerate(words[:-1]):
        next_ = words[i + 1]

        probability = prob_2(word, next_)

        sentence_pro *= probability

    return sentence_pro

print(get_probablity('家庭保险是否覆盖屋顶瓦楞？'))
print('----------------------------------------------')



def get_probablity_(sentence):
    words = cut(sentence)

    sentence_pro = 1

    for i, word in enumerate(words[:-1]):
        next_ = words[i + 1]

        probability = prob_2_(word, next_)

        sentence_pro *= probability

    return sentence_pro
def prob_2_(word1, word2):
    if word1 + word2 in words_count_2:
        #print('{d} in models!'.format(d=word1 + word2))
        return words_count_2[word1+word2] / len(TOKEN_2_GRAM)
    else:
        return 1 / len(TOKEN_2_GRAM)
print(prob_2('保险', '年龄'))

insurance_grammer = """
start == body element statement
statement==投保年龄描述1 | 投保年龄描述2 | 保险期间描述 | 交费方式描述 | 保险金额描述
body == null | 这份保险的 | 该保险的 |  该份保险的 |您买的这份保险的
element == 投保年龄上限 |  投保年龄下限 | 保险期间 | 交费方式 | 保险金额
投保年龄描述1 == 18周岁 | 16周岁 | 0周岁 | 30天 ，
投保年龄描述2== 55周岁 | 60周岁 | 65周岁 | 70周岁 ，
保险期间描述== 1年 | 5年 | 10年 | 30年 | 终身
交费方式描述== 趸交 | 10年交 | 5年交 | 15年交 | 3年交 | 月交 
保险金额描述== 10万元/每份 | 1万元/每份 | 根据投保年龄，交费期限等确定
"""
insurance_grammer=create_grammar(insurance_grammer,split='==')

dict_sorted_predict={}
list_sorted=[]
print('排序前的输出:')
for number in range(20):
    generated_sentence=generate(gram=insurance_grammer, target='start')
    print(generated_sentence)
    list_sorted.append(get_probablity_(generated_sentence))
    dict_sorted_predict[get_probablity_(generated_sentence)]=generated_sentence
list_sorted=sorted(list_sorted,reverse=True)
print('\n\n\n排序后的输出:')
for sorted_sentence in [dict_sorted_predict[number] for number in list_sorted]:
    print(sorted_sentence)






print('------------------------------------------------------------------------------------')
#sys.exit()
##################################################################
###############################################################
#################################################################
###################################################################
#######pattern match
####PROBLEM 1
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
#jieba.cut()
