# Social-Network-Compression

A social network is a network of individuals (such as friends, acquaintances, and coworkers) connected by interpersonal relationships. The number of active users in social media networks is in an exponential rise, creating the need for complex mechanisms to analyze and understand user behavior. One important tool to aid this being the ability to compress these social media networks into graphs that can fit in main memory. This project aims to provide implementations for the state of the art social network compression algorithms (i.e graph compression) based on current research.

There are working implementations based on three methods,
1. Backlinks compression scheme (C++)
2. Slashburn techqnique (Python)
3. Abstract Binary Tree compression (C++)

#### Datasets:

Large Social network graphs can be obtained from [Stanford Large Network Dataset Collection](https://snap.stanford.edu/data/)

#### Note:

+ Edge list format may vary for each implementation, more details are provided in the individual implementations.

+ These implementations are far from perfect but should provide a good base to work upon. Feel free to PR any code improvements (Readability or performance), or any solved issues and feel free to reach out. 

+ The respective folder of each method contains more information on how to run them.

+ ```/data/graph``` contains some sample graphs. 


#### References:

1. Flavio Chierichetti, Ravi Kumar, Silvio Lattanzi, Michael Mitzenmacher,Alessandro Panconesi, and Prabhakar Raghavan. On Compressing Social Networks. In Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD ’09, pages 219–228, New York, NY, USA, 2009. ACM.
2. Yongsub Lim, U. Kang, and C. Faloutsos. SlashBurn: Graph Compression and Mining beyond Caveman Communities. Knowledge and Data Engineering, IEEE Transactions on, 26(12):3077–3089, Dec 2014.
3.  Michael Nelson, Sridhar Radhakrishnan, Amlan Chatterjee, and Chandra Sekharan. Queryable Compression on Streaming Social Networks. In Big Data (Big Data), 2017 IEEE International Conference on, IEEE BigData ’17. IEEE Computer Society, 2017.
