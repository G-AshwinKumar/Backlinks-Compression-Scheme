Abstract Binary Trees compression
========================

Abstract Binary Trees Compression is a graph compression scheme for real-world graphs. ABT compression is a new compression scheme that aims to build a streaming graph system i.e where in new edges can be added to the graphs without having to decompress them entirely.

#### Usage:

Assume graph is stored in some txt file with row-first order (**must** be), and tab separated :

```
0   1
1   0
1   2
2   1
2   3
...
```

(Example data can be found in `data/compressed/Slashdot0902.txt`.)

#### From CUI Interface

    $ make
    $ bin/compress ../data/graph/Slashdot0902.txt opt123.txt

* Execute `make` to build programs.
* Execute `bin/compress` to compress a graph.

#### From Your Program

    AbtCompression bl;
    std::vector<std::pair<int, int> > edge_list;
    BitString compressed_graph;
    
    bl.Compress(edge_list, &compressed_graph);

* Call `Compress` to compress a graph.
* Call `TransformToAdj` and `TransformToEdge` to transform a graph.

#### Note:
Actual compression time will vary depending on system capabilities. The code might crash incase of insufficient ram.

#### References:
1. Michael Nelson, Sridhar Radhakrishnan, Amlan Chatterjee, and Chandra Sekharan. Queryable Compression on Streaming Social Networks. In Big Data (Big Data), 2017 IEEE International Conference on, IEEE BigData ’17. IEEE Computer Society, 2017.
