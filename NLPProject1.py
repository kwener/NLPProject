from pprint import pprint
from operator import itemgetter
import nltk
from nltk.corpus import framenet as fn
from nltk.corpus.reader.framenet import PrettyList

#nltk.download('framenet_v17')
f = fn.frame(202)
print(f.ID)
print(f.name)
print(f.definition)
print(f.frameRelations)
