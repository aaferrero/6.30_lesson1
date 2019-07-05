# 6.30_lesson1
lesson1.py 是课堂内容复现代码
assignment_1.py 是作业1代码
assignment_pattern_match.py 是模式匹配作业代码
联合概率公式有些问题，进行了修改。
def TOKEN_W(w):                                    ###计算不同单词在预料中的次数，为了计算每个词的概率
    return [w1 for w1 in TOKEN if w1==w]


def prob_2_revise(word1, word2):
    if word1 + word2 in words_count_2:
        #print('{d} in models!'.format(d=word1 + word2))
        return words_count_2[word1+word2] / len(TOKEN_W(word2))             ###Pr(w1,w2)=Pr(w1|w2)*Pr(w2)
    else:
        return 1 / len(TOKEN_2_GRAM)

def get_probablity_revise(sentence):                ###修正联合概率公式
    words = cut(sentence)

    sentence_pro = 1

    for i, word in enumerate(words[:-1]):
        next_ = words[i + 1]

        probability = prob_2_revise(word, next_)

        sentence_pro *= probability
    print('sentence_pro',sentence_pro)
    sentence_pro*=len(TOKEN_W(next_))/len(TOKEN_2_GRAM)            ####Pr(w1,w2)=Pr(w1|w2)*Pr(w2)

    return sentence_pro
