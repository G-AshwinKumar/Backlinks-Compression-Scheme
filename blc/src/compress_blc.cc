#include <cstdlib>
#include <iostream>
#include <fstream>
#include <chrono>
#include "backlinks_compression.h"

using namespace std;

bool Input(const char *filename, vector<pair<int, int>> *edges);

int main(int argc, char **argv)
{
  if (argc != 3)
  {
    cerr << "usage: compress GRAPH OUTPUT" << endl;
    exit(EXIT_FAILURE);
  }

  vector<pair<int, int>> edges;
  if (!Input(argv[1], &edges))
  {
    cerr << "error: Load failed" << endl;
    exit(EXIT_FAILURE);
  }
  cout << "Edges      : " << edges.size() << endl;

  BacklinksCompression bl;
  BitString result;
  auto start = std::chrono::high_resolution_clock::now();
  bl.Compress(edges, &result);
  cout << "Bit length : " << result.get_length() << endl;
  cout << "Bits/edge  : " << ((double)result.get_length() / edges.size()) << endl;
  auto finish = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double> elapsed = finish - start;
  cout << "Elapsed time to compress: " << elapsed.count() << " s\n";

  if (!result.Output(argv[2]))
  {
    cerr << "error: Output failed" << endl;
    exit(EXIT_FAILURE);
  }
  exit(EXIT_SUCCESS);
}

bool Input(const char *filename, vector<pair<int, int>> *edges)
{
  ifstream ifs(filename);
  if (!ifs)
    return false;
  for (int v, w; ifs >> v >> w;)
    edges->push_back(make_pair(v, w));
  return !ifs.bad();
}
