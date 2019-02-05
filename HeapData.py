
class HeapData:
    '''
    Created this class to help maintain a heap data structure
    '''

    def __init__(self):
        self.heap = []

    def emptyHeap(self):
        '''
        Emptys the heap
        :return:
        '''

        self.heap = []

    def getHeap(self):
        '''
        :return: array: Returns the heap
        '''

        return self.heap

    def getLeftChildIndex(self, parent_index):
        '''
        :param parent_index: int: index value of the parent in the heap
        :return: int: left child index
        '''

        return (parent_index * 2) + 1

    def getRightChildIndex(self, parent_index):
        '''
        :param parent_index: int: index value of the parent in the heap
        :return: int: right child index
        '''

        return (parent_index * 2) + 2

    def getParentIndex(self, child_index):
        '''
        :param child_index: int: index value of the child node in heap
        :return: int: index of the parent in the heap
        '''

        return (child_index - 1) // 2

    def hasLeftchild(self, index):
        '''
        :param index: int: index value of the child node in heap
        :return: bool: true if present or false
        '''

        return self.getLeftChildIndex(index) < len(self.heap)

    def hasRightchild(self, index):
        '''
        :param index: int: index value of the child node in heap
        :return: bool: true if present or false
        '''

        return self.getRightChildIndex(index) < len(self.heap)

    def hasParent(self, index):
        '''
        :param index: int: index value of the parent node
        :return: bool: true if present or false
        '''

        return self.getParentIndex(index) >= 0

    def leftChild(self, index):
        '''
        :param index: int: index of the parent node
        :return: dict: left child
        '''

        return self.heap[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        '''
        :param index: int: index of the parent node
        :return: dict: right child
        '''

        return self.heap[self.getRightChildIndex(index)]

    def parent(self, index):
        '''
        :param index: int: index of the child node
        :return: dict: parent node
        '''

        return self.heap[self.getParentIndex(index)]

    def swapIndex(self, index_one, index_two):
        '''
        This function is used to swap two values int he heap

        :param index_one: int: index of the first value
        :param index_two: int: index of the second value
        '''

        temp = self.heap[index_one]
        self.heap[index_one] = self.heap[index_two]
        self.heap[index_two] = temp

    def checkForInsertion(self, value):
        '''
        This function checks if a value should be inserted or no

        :param value: dict: value to be inserted
        :return: int: index if it exists or else -1
        '''

        for i in range(len(self.heap) // 2, len(self.heap)):
            if value["probability"] > self.heap[i]["probability"]:
                return i
        return -1

    def addToHeap(self, value, beamK):
        '''
        This function is used to add values to the heap

        :param value: dict: value to be added
        :param beamK: int: length of the heap
        '''

        if not self.heap:
            self.heap.append(value)
        else:
            if len(self.heap) > beamK:
                self.heap.append(value)
                self.heapifyUp()
            else:
                index = self.checkForInsertion(value)
                if index != -1:
                    self.heap[index] = value
                    self.heapifyUp(index)

    def heapifyUp(self, index=None):
        '''
        This function is called when a value is added
        at the end of the heap

        :param index: int: index value, if not the last element
        :return:
        '''

        if index == None:
            index = len(self.heap) - 1
        while self.hasParent(index) and self.parent(index)["probability"] < self.heap[index]["probability"]:
            self.swapIndex(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        '''
        This function is called when a value if
        added to the start of the heap
        '''

        index = 0
        while self.hasLeftchild(index):
            smaller_child_index = self.getLeftChildIndex(index)
            if self.hasRightchild(index) and self.heap[smaller_child_index]["probability"] > self.rightChild(index)["probability"]:
                smaller_child_index = self.getRightChildIndex(index)
            if self.heap[smaller_child_index]["probability"] < self.heap[index]["probability"]:
                break
            else:
                self.swapIndex(smaller_child_index, index)
            index = smaller_child_index


