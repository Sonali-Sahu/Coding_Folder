from mrjob.job import MRJob
import re


class WordCount(MRJob):
    # mapper function
    def mapper(self, _, line):
        words = re.findall(r'\w+', line.lower())
        for word in words:
            yield word, 1

    # Reducer function
    def reducer(self, word, counts):
        yield word, sum(counts)


WordCount.run()
