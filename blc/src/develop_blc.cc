#include <stdint.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <chrono>
#include "backlinks_compression.h"

using namespace std;

bool Output(const char *filename, vector<pair<int, int>> &edges);

int main(int argc, char **argv)
{
  if (argc != 3)
  {
    cerr << "usage: develop GRAPH OUTPUT" << endl;
    exit(EXIT_FAILURE);
  }

  BitString compressed_graph;
  if (!compressed_graph.Input(argv[1]))
  {
    cerr << "error: Load failed" << endl;
    exit(EXIT_FAILURE);
  }

  BacklinksCompression bl;
  vector<pair<int, int>> edges;
  auto start = std::chrono::high_resolution_clock::now();
  bl.Develop(compressed_graph, &edges);
  auto finish = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double> elapsed = finish - start;
  cout << "Elapsed time to decompress: " << elapsed.count() << " s\n";

  if (!Output(argv[2], edges))
  {
    cerr << "error: Output failed" << endl;
    exit(EXIT_FAILURE);
  }
  exit(EXIT_SUCCESS);
}

bool Output(const char *filename, vector<pair<int, int>> &edges)
{
  ofstream ofs(filename);
  if (!ofs)
    return false;
  for (uint64_t i = 0; i < edges.size(); ++i)
  {
    ofs << edges[i].first << "\t" << edges[i].second << endl;
  }
  return ofs.good();
}
