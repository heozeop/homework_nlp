# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import math, heapq
from operator import itemgetter

class VSModel: 
    def __init__(self, movie_scripts, preprocessor):
        self.preprocessor = preprocessor
        self.doc_len = len(movie_scripts)
        self.index = self.get_inverted_index(movie_scripts)
        print(len(self.index))
    
    def script_to_key_list(self, movie_script):
        return self.preprocessor.preprocess(movie_script)
    
    def check_keyword_frequency(self, raw_keywords):
        keyword_dict = {key: 0 for key in list(set(raw_keywords))}
        
        for keyword in raw_keywords:
            keyword_dict[keyword] += 1

        return keyword_dict
    
    def get_inverted_index(self, movie_raw):
        index = {}
        doc_len = len(movie_raw)
        
        for i, movie_script in enumerate(movie_raw):
            key_list = self.script_to_key_list(movie_script)
            key_dict = self.check_keyword_frequency(key_list)
            
            key_list = list(set(key_list))  # make unique set
            
            for key in key_list:            
                h = [] 
                tf = 1 + math.log(key_dict[key], 2)
                h.append((tf, i))

                if key in index:
                    index[key][1].extend(h)
                else:
                    index[key] = (key_dict[key], h)
                
        return index;
    
        
    def parse_to_tf_idf(self, term):
        if (term in self.index) is False:
            return None
        
        (df, tf_list) = self.index[term]
        idf = math.log(self.doc_len/len(tf_list),2)
        
        return [(item[0] * idf, item[1]) for item in tf_list]
                             
    def calc_similarity(self, term_list):
        doc = {}
        for term in term_list:
            tf_idf_list = self.parse_to_tf_idf(term)
            
            if tf_idf_list != None:
                for tf_idf, di in tf_idf_list:
                    if di in doc:
                        doc[di] += tf_idf
                    else:
                        doc[di] = tf_idf
        return doc
    
    def query(self, text, k):

        term_list = self.script_to_key_list(text)
 
        docs = self.calc_similarity(self.check_keyword_frequency(term_list))

        return heapq.nlargest(k,docs.items(), key=itemgetter(1))


# %%
stop_words = "a's, able, im, uh, about, cod't, cont'd, above, according, accordingly, across, actually, after, afterwards, again, against, ain’t, all, allow, allows, almost, alone, along, already, also, although, always, am, among, amongst, an, and, another, any, anybody, anyhow, anyone, anything, anyway, anyways, anywhere, apart, appear, appreciate, appropriate, are, aren’t, around, as, aside, ask, asking, associated, at, available, away, awfully, be, became, because, become, becomes, becoming, been, before, beforehand, behind, being, believe, below, beside, besides, best, better, between, beyond, both, brief, but, by, c’mon, c’s, came, can, can’t, cannot, cant, cause, causes, certain, certainly, changes, clearly, co, com, come, comes, concerning, consequently, consider, considering, contain, containing, contains, corresponding, could, couldn’t, course, currently, definitely, described, despite, did, didn’t, different, do, does, doesn’t, doing, don’t, done, down, downwards, during, each, edu, eg, eight, either, else, elsewhere, enough, entirely, especially, et, etc, even, ever, every, everybody, everyone, everything, everywhere, ex, exactly, example, except, far, few, fifth, first, five, followed, following, follows, for, former, formerly, forth, four, from, further, furthermore, get, gets, getting, given, gives, go, goes, going, gone, got, gotten, greetings, had, hadn’t, happens, hardly, has, hasn’t, have, haven’t, having, he, he’s, hello, help, hence, her, here, here’s, hereafter, hereby, herein, hereupon, hers, herself, hi, him, himself, his, hither, hopefully, how, howbeit, however, i, i’d, i’ll, i’m, i’ve, ie, if, ignored, immediate, in, inasmuch, inc, indeed, indicate, indicated, indicates, inner, insofar, instead, into, inward, is, isn’t, it, it’d, it’ll, it’s, its, itself, just, keep, keeps, kept, know, knows, known, last, lately, later, latter, latterly, least, less, lest, let, let’s, like, liked, likely, little, look, looking, looks, ltd, mainly, many, may, maybe, me, mean, meanwhile, merely, might, more, moreover, most, mostly, much, must, my, myself, name, namely, nd, near, nearly, necessary, need, needs, neither, never, nevertheless, new, next, nine, no, nobody, non, none, noone, nor, normally, not, nothing, novel, now, nowhere, obviously, of, off, often, oh, ok, okay, old, on, once, one, ones, only, onto, or, other, others, otherwise, ought, our, ours, ourselves, out, outside, over, overall, own, particular, particularly, per, perhaps, placed, please, plus, possible, presumably, probably, provides, que, quite, qv, rather, rd, re, really, reasonably, regarding, regardless, regards, relatively, respectively, right, said, same, saw, say, saying, says, second, secondly, see, seeing, seem, seemed, seeming, seems, seen, self, selves, sensible, sent, serious, seriously, seven, several, shall, she, should, shouldn’t, since, six, so, some, somebody, somehow, someone, something, sometime, sometimes, somewhat, somewhere, soon, sorry, specified, specify, specifying, still, sub, such, sup, sure, t’s, take, taken, tell, tends, th, than, thank, thanks, thanx, that, that’s, thats, the, their, theirs, them, themselves, then, thence, there, there’s, thereafter, thereby, therefore, therein, theres, thereupon, these, they, they’d, they’ll, they’re, they’ve, think, third, this, thorough, thoroughly, those, though, three, through, throughout, thru, thus, to, together, too, took, toward, towards, tried, tries, truly, try, trying, twice, two, un, under, unfortunately, unless, unlikely, until, unto, up, upon, us, use, used, useful, uses, using, usually, value, various, very, via, viz, vs, want, wants, was, wasn’t, way, we, we’d, we’ll, we’re, we’ve, welcome, well, went, were, weren’t, what, what’s, whatever, when, whence, whenever, where, where’s, whereafter, whereas, whereby, wherein, whereupon, wherever, whether, which, while, whither, who, who’s, whoever, whole, whom, whose, why, will, willing, wish, with, within, without, won't, wonder, would, would, wouldn't, yes, yet, you, you'd, you'll, you're, you've, your, yours, yourself, yourselves, zero".replace('’',"'").split(', ')

end_words = '|'.join(['\,','\.','\?','\!','\-','\:','\;','\r','\n','\t','\(','\)','\{','\}',"\'s","\_","\&", "\#", "\@", "\#","\^","\*","\/","\[","\]"])

from nltk.stem import PorterStemmer


# %%
import re

class Preprocessor:

    
    def __init__(self, stop_words, end_words, stemmer):
        self.stop_words = stop_words
        self.end_words = end_words
        self.stemmer = stemmer
        
    def preprocess(self, raw_data):
        tokenized_data = self.tokenize(raw_data)
        stemmed_data = self.stemming(tokenized_data)
        
        return stemmed_data
    
    def tokenize(self, data):
        # replace end words with space
        end_replaced = re.sub(self.end_words, " ", data.lower())
        
        # split
        script_chunks = end_replaced.split(' ')
        
        # remove stop_wrods
        filtered_script = filter(lambda x: len(x) > 1 and ((x in stop_words) is False), script_chunks)
        
        return ["{}".format(key.replace('"', "").replace("'","")) for key in list(filtered_script)]
    
    def stemming(self, words):
        return [self.stemmer.stem(word) for word in words]
    
    def check_keyword_frequency(self, raw_keywords):
        keyword_dict = {key: 0 for key in list(set(raw_keywords))}
        
        for keyword in raw_keywords:
            keyword_dict[keyword] += 1

        return keyword_dict
    


# %%
processor = Preprocessor(stop_words=stop_words, end_words=end_words, stemmer=PorterStemmer())


# %%
import json
f = open('./data/grouped_by_genre/raw/Musical.json', 'r')
movie_scripts = json.loads(f.read())
movie_scripts = [movie[1] for movie in movie_scripts]


# %%
a = VSModel(movie_scripts, processor)


# %%
a.query('i love you',10)


# %%



# %%



