from scanner import Scanner
from graph import Graph

scanner = Scanner("images")
graph = Graph()
dists = scanner.find_dists()
graph.view(dists)
