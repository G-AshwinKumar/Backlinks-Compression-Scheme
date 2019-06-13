# Slashburn

Slashburn tried to exploit the hubs and the neighbors (‘spokes’) of the hubs to define an alternative community different from the traditional community. It is based on the observation that real world graphs are easily disconnected by hubs, or high degree nodes: removing hubs from a graph creates many small disconnected components, and the remaining giant connected component is substantially smaller than the original graph. The method aims to order these hubs and spokes to get such a compact representation of the adjacency matrix, which in turn leads to good compression. 

In its essence Slashburn is a reodering algorithm following which running standard compression algorithms such as gzip, bz2 and 7z yield better compression.

---

### Requirements

* `scipy`
* `numpy`
* `pandas`
* `os`
* `pickle`
---

### Usage

Assume graph is stored in some txt file with row-first order (**must** be):
```
0,1
1,0
1,2
2,1
2,3
...
```
(Example data can be found in `data/compressed/Slashdot0811.txt`.)

You can run the slashburn algorithm using,

```python
import numpy as np
from ppr import PPRBear as Bear
bear = Bear()
bear.preprocess('data/small.csv')
```

+ Then use any standard compression engine such as [7zip](https://www.7-zip.org/) to compress the reordered schema.
+ Sample execution for the slashburn algorithm is in ash.py file. Take a look at that file for deailed usage explanation.
---
#### Note:
Actual compression time will vary depending on system capabilities. The code might crash incase of insufficient ram.
---
### References:
+ Yongsub Lim, U. Kang, and C. Faloutsos. SlashBurn: Graph Compression and Mining beyond Caveman Communities. Knowledge and Data Engineering, IEEE Transactions on, 26(12):3077–3089, Dec 2014.
