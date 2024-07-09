class WordsFinder:
    file_names = ()

    def __init__(self, *args):
        self.args = args
        self.file_names += args

    def get_all_words(self):
        all_words = {}
        for file_ in self.file_names:
            list_ = []
            list_1 = [',', '.', '=', '!', '?', ';', ':', '-', "'"]
            with open(file_, encoding='utf-8') as fail_2:
                for i in fail_2:
                    for q in i:
                        if q not in list_1:
                            list_.append(q.lower())
            a = ''.join(list_)
            d = a.split()
            all_words[file_] = d

        return all_words

    def find(self, word):
        dict_ = dict()
        word = str(word).lower()
        for name, words in self.get_all_words().items():
            if word in words:
                dict_[name] = words.index(word) + 1
        return dict_

    def count(self, word):
        dict_ = dict()
        word = str(word).lower()
        for name, words in self.get_all_words().items():
            if word in words:
                dict_[name] = words.count(word)
        return dict_


# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))
#

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
#
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
print(finder1.get_all_words())
print(finder1.find('child'))
print(finder1.count('child'))
