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
    cerr << "Incorrect number of arguments check usage for info" << endl;
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
  string result = argv[2];
  auto start = std::chrono::high_resolution_clock::now();
  bl.Compress(edges, result);
  streampos begin, end;
  ifstream myfile(result.c_str(), ios::binary);
  begin = myfile.tellg();
  myfile.seekg(0, ios::end);
  end = myfile.tellg();
  myfile.close();
  long size = (end - begin) * 8;
  cout << "Bit length : " << size << endl;
  cout << "Bits/edge  : " << ((double)size / edges.size()) << endl;
  auto finish = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double> elapsed = finish - start;
  cout << "Elapsed time to compress: " << elapsed.count() << " s\n";
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
