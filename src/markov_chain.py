from random import random

class MarkovChain(object):
    def __init__(self, transition_matrix_: list[list[float]], states_: list=None) -> None:
        self.transition_matrix = transition_matrix_
        self.normalize()

        self.states = states_

        self.state = -1

    def normalize(self) -> None:
        normalized: list = list()
        for state_probs in self.transition_matrix:
            sum_ = sum(state_probs)
            normalized.append([prob/sum_ for prob in state_probs])
        self.transition_matrix = normalized

    def next(self) -> int:
        if self.state < 0:
            return -1

        pick = random()
        p = 0.0
        for n, prob in enumerate(self.transition_matrix[self.state]):
            p += prob
            if p >= pick:
                return n 

        return -1

    def produce(self, length: int, start: int=0) -> list[int]:
        chain: list = [start]
        self.state = start  

        for i in range(length-1):
            s = self.next()
            self.state = s
            chain.append(s)

        return chain

    def translate(self, chain: list[int]) -> list:
        if self.states is not None:
            return [self.states[i] for i in chain if i < len(self.states)]
        else:
            return chain