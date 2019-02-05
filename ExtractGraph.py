class ExtractGraph:
    '''
    In this class we read an input .txt file and convert it
    into a directed weighted graph

    '''

    # key is head word; value stores next word and corresponding probability.
    def __init__(self):
        '''
        Reads the .txt file and converts it to an array of sentences.
        It then calls the createGraph() method to create a graph of the data structure
        '''

        # Extract the directed weighted graph, and save to {head_word, [{tail_word, probability}]}
        self.graph = {}
        self.sentences_add = "data\\assign1_sentences_complete.txt"
        self.data = open(self.sentences_add, "r")
        print("Extracting sentences and creating a directed weighted graph")
        self.createGraph()
        print("Graph is ready to use")
        return

    def createGraph(self):
        '''
        Creates a directed weighted graph of each word. Every word has
        a child word associated to it with a probability of how likely
        it is to occur, along with a count of the number of times the word has appeared.
        eg: hello : {there: {probability: 0.5, count: 1}, how: {probability: 0.5, count: 1}}

        :return: self.graph: dict: A dictionary of all the words
        '''

        if not len(self.graph):
            for sentence in self.data:
                words = sentence.split()
                check = 0
                for x in range(1, len(words)):
                    full_count = 0
                    if str(words[check]) in self.graph.keys():
                        if str(words[x]) in self.graph[str(words[check])]:
                            self.graph[str(words[check])][str(words[x])]["count"] = \
                                int(self.graph[str(words[check])][str(words[x])]["count"]) + 1
                        else:
                            self.graph[str(words[check])][str(words[x])] = {"probability": 1.0, "count": 1}
                        for tail_words in self.graph[str(words[check])]:
                            full_count = full_count + self.graph[str(words[check])][tail_words]['count']
                        for tail_words in self.graph[str(words[check])]:
                            self.graph[str(words[check])][tail_words]['probability'] = \
                                int(self.graph[str(words[check])][tail_words]['count']) / \
                                full_count
                    else:
                        self.graph[str(words[check])] = {str(words[x]): {"probability": 1.0, "count": 1}}
                    check = x
        return self.graph

    def getProb(self, head_word, tail_word):
        '''
        It fetches the probability of the tail_word coming after the head_word

        :param head_word: string: The head word
        :param tail_word: string: The tail word
        :return: float: probability of the word occurring
        '''

        if str(tail_word) in self.graph[str(head_word)]:
            return self.graph[str(head_word)][str(tail_word)]['probability']
        return 0
