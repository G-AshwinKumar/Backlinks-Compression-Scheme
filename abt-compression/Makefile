CXX = g++
CXXFLAGS = -g -Wall -Wextra -Wno-sign-compare -O3 -std=c++1z
SOURCES = src/abt_compression.h src/abt_compression.cc

LIB = -lgtest -lgtest_main -lpthread
GTEST_ROOT= lib/gtest-1.6.0

all: bin bin/compress

test: bin/test

bin:
	mkdir -p bin

bin/compress: src/compress_main.cc ${SOURCES}
	$(CXX) $(CXXFLAGS) -Isrc -o $@ $^

bin/test: src/abt_compression_test.cc ${SOURCES} 
	$(CXX) $(CXXFLAGS) -o $@ $^ -I $(GTEST_ROOT)/include -L $(GTEST_ROOT)/lib $(LIB)
	./$@

.PHONY:	test clean

clean:
	rm -rf bin
