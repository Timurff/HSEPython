import ast

import astunparse
import networkx as nx
import matplotlib.pyplot as plt


class VisitAST(ast.NodeVisitor):
    def __init__(self):
        super(ast.NodeVisitor, self).__init__()
        self.graph = nx.Graph()
        self.stack = []

    def create_edges(self, node_name):
        parent_name = None
        if len(self.stack) != 0:
            parent_name = self.stack[-1]

        self.stack.append(node_name)
        self.graph.add_node(node_name)

        if parent_name:
            self.graph.add_edge(node_name, parent_name)

    def proceed(self, node, node_name):
        self.create_edges(node_name)
        super(self.__class__, self).generic_visit(node)
        self.stack.pop()

    def generic_visit(self, node):
        try:
            node_name = astunparse.unparse(node)
            self.proceed(node, node_name)
        except AttributeError:
            super(self.__class__, self).generic_visit(node)

    def visit_FunctionDef(self, node):
        node_name = node.name
        self.proceed(node, node_name)


def main():
    walker = VisitAST()
    filename = 'fibonacci.py'

    with open(filename, 'r') as fin:
        src = fin.read()

    fig, ax = plt.subplots(figsize=(25, 25))

    node = ast.parse(src)
    walker.visit(node)
    nx.draw(walker.graph, with_labels=True, ax=ax)

    plt.savefig('artifacts/ast_fibonacci_ugly_one.png')


if __name__ == '__main__':
    main()
