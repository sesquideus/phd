class Trie():
    def __init__(self):
        self.children = {}
        self.terminal = False

    def add(self, what):
        if len(what) == 0:
            self.terminal = True
        else:
            char = what[0]
            if not char in self.children:
                self.children[char] = Trie()

            self.children[char].add(what[1:])

    def __str__(self, prefix=''):
        return ', '.join(self.__repr__())

    def __repr__(self, prefix=''):
        other = sum([child.__repr__(prefix + char) for char, child in self.children.items()], [])
        if self.terminal:
            return [prefix] + other
        else:
            return other


root = Trie()

with open('../trojsten/5000.txt', 'r') as f:
    for line in f.readlines():
        kline = line.rstrip('\n')
        root.add(kline)
        print(kline)

matrix = [['c', 'e', 'č', 'e'], ['k', 'i', 'n', 'k'], ['a', 'l', 'e', 'a'], ['p', 't', 'k', 'v']]

print(root.__repr__())
