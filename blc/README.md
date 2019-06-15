Backlinks compression
========================

Backlinks compression is a graph compression scheme for real-world graphs. Backlinks compression (BLC) draws inspiration from the seminal paper by Boldi and Vigna (BV) on WebGraph compression. 

BV incorporates three main ideas,
+ Locality
+ Similarity
+ Gap encoding

BLC expands on this by incorporating another idea namely, 
+ Reciprocity

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
    $ bin/compress ../data/graph/graph_file.txt ../data/compressed/compressed_graph_file.dat
    $ bin/develop ../data/compressed/compressed_graph_file.dat ../data/graph/original_graph.txt

Sample execution,

```
make
bin/compress ../data/graph/Slashdot0902.txt ../data/compressed/output.dat
bin/develop ../data/compressed/output.dat ../data/graph/original_graph.txt
```

* Execute `make` to build programs.
* Execute `bin/compress` to compress a graph.
* Execute `bin/develop` to develop a compressed graph.

#### From Your Program

    BacklinksCompression bl;
    std::vector<std::pair<int, int> > edge_list;
    BitString compressed_graph;
    bl.Compress(edge_list, &compressed_graph);
    bl.Develop(compressed_graph, &edge_list);

* Call `Compress` to compress a graph.
* Call `Develop` to develop a compressed graph.
* Call `TransformToAdj` and `TransformToEdge` to transform a graph.

#### Performance

Backlinks compression scheme has two steps: ordering vertices and encoding the graph.
This implementation uses BFS ordering for ordering vertices and δ-code as the integer encoding scheme in encoding the graph.

The followings are the results for real graphs in [Stanford Large Network Dataset Collection](http://snap.stanford.edu/data/).

    graph : soc-Slashdot0922
    Edges      : 948464
    Bit length : 9238812
    Bits/edge  : 9.74081
    Elapsed time to compress: 2.16511s
    
    graph : soc-LiveJournal
    Edges      : 68993773
    Bit length : 937623773
    Bits/edge  : 13.59
    Elapsed time to compress: 122.133s
    
#### Note:
Actual compression time will vary depending on system capabilities. The code might crash incase of insufficient ram.

#### References

* Flavio Chierichetti, Ravi Kumar, Silvio Lattanzi, Michael Mitzenmacher,Alessandro Panconesi, and Prabhakar Raghavan. On Compressing Social Networks. In Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD ’09, pages 219–228, New York, NY, USA, 2009. ACM.

* P. Boldi and S. Vigna. The Webgraph Framework I: Compression Techniques. In Proceedings of the 13th International Conference on World Wide Web, WWW ’04, pages 595–602, New York, NY, USA, 2004. ACM.
