import runpy

dimensions = [10, 30, 50, 100]

for dimension in dimensions:
    for k in range (1, dimension+1):
        runpy.run_path('plot-graph.py', init_globals={'dimension': dimension, 'number_of_element': k})
    