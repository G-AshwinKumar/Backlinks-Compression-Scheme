# Slashburn

Python implementation of [SlashBurn][2]

---

### Requirements

* `scipy`
* `numpy`
* `pandas`
* few other modules look at .py files

---

### Usage

Assume graph is store in some txt file named `Slashdot0811.txt` with row-first order (**must** be):
```
0,1
1,0
1,2
2,1
2,3
...
```
(Example data can be found in `data/compressed/Slashdot0811.txt`.)
You can run the slashbunr algorithm using 
```python
import numpy as np
from ppr import PPRBear as Bear
bear = Bear()
bear.preprocess('data/small.csv')
```
Sample execution is in ash.py file. Take a look at that file for deailed usage explanation.

---

[1]: http://dl.acm.org/citation.cfm?id=2723716
[2]: http://ieeexplore.ieee.org/abstract/document/6807798/
[3]: https://datalab.snu.ac.kr/bear/
