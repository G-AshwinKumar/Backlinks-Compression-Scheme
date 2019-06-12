Abstract Binary Trees compression
========================

Abstract Binary Trees Compression is a graph compression scheme for real-world graphs.

### From CUI Interface

    $ make
    $ bin/compress samples/graph_example.tsv output_file.dat

* Execute `make` to build programs.
* Execute `bin/compress` to compress a graph.

### From Your Program

    AbtCompression bl;
    std::vector<std::pair<int, int> > edge_list;
    BitString compressed_graph;
    
    bl.Compress(edge_list, &compressed_graph);

* Call `Compress` to compress a graph.
* Call `TransformToAdj` and `TransformToEdge` to transform a graph.

#Performance


The followings are the results for real graphs in [Stanford Large Network Dataset Collection](http://snap.stanford.edu/data/).

