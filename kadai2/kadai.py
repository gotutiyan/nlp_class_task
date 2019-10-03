import math

def make_tf(words, tags):
    tf = dict()
    # タグを登録
    for t in tags:
        if tf.get(t) == None:
            tf.update({t:{}})

    for i in range(len(tags)):
        for word in words[i]:
            if tf[tags[i]].get(word) == None:
                for tag in tf.keys():
                    tf[tag].update({word:0})
                tf[tags[i]][word] = 1
            else:
                tf[tags[i]][word] += 1
    return tf

def make_idf(tf):
    idf = dict()
    for tag in tf.keys():
        for word in tf[tag].keys():
            if tf[tag][word] == 0:
                continue
            if idf.get(word) == None:
                idf.update({word:1})
            else:
                idf[word] += 1
    
    for word in idf.keys():
        idf[word] = (math.log(len(tf)/idf[word], 10) + 1)
    return idf

def make_tf_idf(tf, idf):
    tf_idf = tf
    for tag in tf.keys():
        for word in tf[tag].keys():
            tf_idf[tag][word] = tf[tag][word] * idf[word]
    return tf_idf


class Score:
    def __init__(self, tag, score):
        self.tag = tag
        self.score = score


def k_nearest(k, tf_idf, index_word):
    top = list(tf_idf.keys())[0]
    index_vec = [0 for i in range(len(tf_idf[top]))]
    word2num = dict()
    cnt = 0
    for word in tf_idf[top].keys():
        word2num.update({word:cnt})
        cnt += 1
    for iw in index_word:
        if word2num.get(iw) != None:
            index_vec[word2num[iw]] = 1
    rank = []
    for tag in tf_idf.keys():
        score =0
        cnt = 0
        for word in tf_idf[tag].keys():
            score += tf_idf[tag][word] * index_vec[cnt]
            cnt += 1
        rank.append(Score(tag, score))
    
    rank.sort(key = lambda s:s.score, reverse = True)
    return rank[:k]

def show_k_nearest(k, tf_idf):
    with open("./input_index.csv")as f:
        for line in f:
            line = line.strip()
            line = line.split(',')
            result = k_nearest(k, tf_idf, line)
            print([s.tag for i,s in enumerate(result)])
    pass
    
def main():
    words = []
    tags = []
    with open("train.csv")as f:
        for data in f:
            data = data.split('\t')
            words.append(data[0].split(','))
            tags.append(data[1].strip())
    tf = make_tf(words,tags)
    idf = make_idf(tf)
    tf_idf = make_tf_idf(tf, idf)
    show_k_nearest(3, tf_idf)

if __name__ == "__main__":
    main()