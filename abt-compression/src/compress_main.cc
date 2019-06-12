#include <cstdlib>
#include <iostream>
#include <fstream>
#include <chrono>
#include "abt_compression.h"

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

  AbtCompression bl;
  BitString result;
  auto start = std::chrono::high_resolution_clock::now();
  /* for (const auto &p : edges)
  {
    std::cout << p.first << ", " << p.second << std::endl;
    // or std::cout << std::get<0>(p) << ", " << std::get<1>(p) << std::endl;
  } */
  bl.Compress(edges, &result);
  auto finish = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double> elapsed = finish - start;
  //std::ifstream in_file("opt11.txt", std::ios::binary | std::ios::ate);
  //int file_size = in_file.tellg();
  //file_size*=8;
  //cout << "Bit length : " << file_size << endl;
  //cout << "Bits/edge  : " << ((double)file_size / edges.size()) << endl;
  //cout << "Elapsed time to compress: " << elapsed.count() << " s\n";

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
