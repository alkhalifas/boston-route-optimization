import pandas as pd
import numpy as np


class BostonMap:
    def __init__(self):
        self.city_name = "Boston"
        self.adjacency_matrix = []
        self.adjacency_list = {}
        self.nodes = {}

    def add_node(self, node):
