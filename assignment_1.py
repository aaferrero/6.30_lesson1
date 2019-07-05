import random


print('------------------------------------asignment 1.1')
def create_grammar(grammar_str, split='=>', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip():
            continue
        exp, stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
        #print(grammar[exp.strip()])
    return grammar



choice = random.choice


def generate(gram, target):
    if target not in gram:
        return target  # means target is a terminal expression
    choice1=choice(gram[target])

    expaned = [generate(gram, t) for t in choice(gram[target])]
    #print(111,expaned)
    return ''.join([e if e != '/n' else '\n' for e in expaned if e != 'null'])



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
print('------------------------------------asignment 1.2')

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

