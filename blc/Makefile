CXX = g++
CXXFLAGS = -g -Wall -Wextra -Wno-sign-compare -O3 -std=c++0x
SOURCES = src/backlinks_compression.h src/backlinks_compression.cc

LIB = -lgtest -lgtest_main -lpthread
GTEST_ROOT= lib/gtest-1.6.0

all: bin bin/compress bin/develop

test: bin/test

bin:
	mkdir -p bin

bin/compress: src/compress_blc.cc ${SOURCES}
	$(CXX) $(CXXFLAGS) -Isrc -o $@ $^

bin/develop: src/develop_blc.cc ${SOURCES}
	$(CXX) $(CXXFLAGS) -Isrc -o $@ $^

bin/test: src/backlinks_compression_test.cc ${SOURCES} 
	$(CXX) $(CXXFLAGS) -o $@ $^ -I $(GTEST_ROOT)/include -L $(GTEST_ROOT)/lib $(LIB)
	./$@

.PHONY:	test clean

clean:
	rm -rf bin
