import StringDouble
import ExtractGraph
import HeapData

class BeamSearch:
    '''
    This class performs Beam Search on the directed weighted graph
    '''

    graph = []
    HeapData = HeapData.HeapData()

    def __init__(self, input_graph):
        '''
        Calls the createGraph() method to create the graph

        :param input_graph: object: object of the class ExtracGraph
        '''

        self.graph = input_graph.createGraph()
        return

    def beamSearch(self, pre_words, beamK, maxToken):
        '''
        Performes beam search on the directed graph. MaxToken is the
        maximum allowed words in the sentence and beamK is the width
        of the beam.

        :param pre_words: string: sentence for completion
        :param beamK: int: width of the beam
        :param maxToken: int: maximum words allowed
        :return:
            sentence: string: Complete sentence
            probability: float: probability of the sentence
        '''

        all_words = pre_words.split()
        length = len(all_words)
        output_heap = [{"sentence": pre_words, "probability": 1}]
        self.HeapData.emptyHeap()
        while length <= maxToken:
            # Goes through all the last words in the heap
            for word in output_heap:
                last_word = word["sentence"].split()
                last_word = last_word[len(last_word) - 1]
                if str(last_word) in self.graph.keys():
                    for key in self.graph[str(last_word)]:
                        if key != "</s>":
                            probability = word["probability"] * self.graph[last_word][key]["probability"]
                            self.HeapData.addToHeap({
                                "sentence": word["sentence"] + " " + key,
                                "probability": probability,
                            }, beamK)
                        else:
                            self.HeapData.addToHeap({
                                "sentence": word["sentence"] + " " + key,
                                "probability": word["probability"],
                            }, beamK)
                if str(last_word) == "</s>":
                    self.HeapData.addToHeap({
                        "sentence": word["sentence"],
                        "probability": word["probability"],
                    }, beamK)
            output_heap = self.HeapData.getHeap()
            length += 1
            self.HeapData.emptyHeap()

        return StringDouble.StringDouble(output_heap[0]["sentence"], output_heap[0]["probability"])
