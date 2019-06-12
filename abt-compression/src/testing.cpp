#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdint.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <time.h>
using namespace std;

class bitChar
{
public:
    unsigned char *c;
    int shift_count;
    string BITS;

    bitChar()
    {
        shift_count = 0;
        c = (unsigned char *)calloc(1, sizeof(char));
    }

    string readByBits(ifstream &inf)
    {
        string s = "";
        char buffer[1];
        while (inf.read(buffer, 1))
        {
            s += getBits(*buffer);
        }
        return s;
    }

    void setBITS(string X)
    {
        BITS = X;
    }

    int insertBits(ofstream &outf)
    {
        int total = 0;

        while (BITS.length())
        {
            if (BITS[0] == '1')
                *c |= 1;
            *c <<= 1;
            ++shift_count;
            ++total;
            BITS.erase(0, 1);

            if (shift_count == 7)
            {
                if (BITS.size() > 0)
                {
                    if (BITS[0] == '1')
                        *c |= 1;
                    ++total;
                    BITS.erase(0, 1);
                }

                writeBits(outf);
                shift_count = 0;
                free(c);
                c = (unsigned char *)calloc(1, sizeof(char));
            }
        }

        if (shift_count > 0)
        {
            *c <<= (7 - shift_count);
            writeBits(outf);
            free(c);
            c = (unsigned char *)calloc(1, sizeof(char));
        }
        outf.close();
        return total;
    }

    string getBits(unsigned char X)
    {
        stringstream itoa;
        for (unsigned s = 7; s > 0; s--)
        {
            itoa << ((X >> s) & 1);
        }

        itoa << (X & 1);
        return itoa.str();
    }

    void writeBits(ofstream &outf)
    {
        outf << *c;
    }

    ~bitChar()
    {
        if (c)
            free(c);
    }
};

int main()
{
    ofstream outf("Sample.dat", std::ios_base::app);
    ifstream inf("Sample.dat");

    string enCoded = "11110001100110011";
    std::vector<int> temp_array(10, -1);
    temp_array[0] = 1;
    temp_array[1] = 1;
    temp_array[2] = 0;
    temp_array[4] = 1;
    temp_array[6] = 0;
    temp_array[7] = 1;
    temp_array[8] = 1;
    temp_array[9] = 0;
    std::string str;

    for (int k = 0; k < 10; k++)
    {
        // cout << temp_array[k];
        if (temp_array[k] != -1)
        {

            str.push_back('0' + temp_array[k]);
        }
    }
    //write to file

    cout << "Str" << str << endl;
    bitChar bchar;
    bchar.setBITS(str);
    bchar.insertBits(outf);
    bchar.setBITS(str);
    bchar.insertBits(outf);

    //read from file
    string decoded = bchar.readByBits(inf);
    cout << "Decoded" << decoded << endl; //print 101000001010101010000000
    return 0;
}