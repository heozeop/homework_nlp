import math, heapq
from operator import itemgetter


def check_keyword_frequency(raw_keywords):
    keyword_dict = {key: 0 for key in list(set(raw_keywords))}

    for keyword in raw_keywords:
        keyword_dict[keyword] += 1

    return keyword_dict


class VSModel:
    def __init__(self, movie_scripts, preprocessor):
        self.preprocessor = preprocessor
        self.doc_len = len(movie_scripts)
        self.index = self.get_inverted_index(movie_scripts)
        print(len(self.index))

    def script_to_key_list(self, movie_script):
        return self.preprocessor.preprocess(movie_script)

    def get_inverted_index(self, movie_raw):
        index = {}
        doc_len = len(movie_raw)

        for i, movie_script in enumerate(movie_raw):
            key_list = self.script_to_key_list(movie_script)
            key_dict = check_keyword_frequency(key_list)

            key_list = list(set(key_list))  # make unique set

            for key in key_list:
                h = []
                tf = 1 + math.log(key_dict[key], 2)
                h.append((tf, i))

                if key in index:
                    index[key][1].extend(h)
                else:
                    index[key] = (key_dict[key], h)

        return index

    def parse_to_tf_idf(self, term):
        if (term in self.index) is False:
            return None

        (df, tf_list) = self.index[term]
        idf = math.log(self.doc_len / len(tf_list), 2)

        return [(item[0] * idf, item[1]) for item in tf_list]

    def calc_similarity(self, term_list):
        doc = {}
        for term in term_list:
            tf_idf_list = self.parse_to_tf_idf(term)

            if tf_idf_list is not None:
                for tf_idf, di in tf_idf_list:
                    if di in doc:
                        doc[di] += tf_idf
                    else:
                        doc[di] = tf_idf
        return doc

    def query(self, text, k):

        term_list = self.script_to_key_list(text)

        docs = self.calc_similarity(check_keyword_frequency(term_list))

        return heapq.nlargest(k, docs.items(), key=itemgetter(1))
