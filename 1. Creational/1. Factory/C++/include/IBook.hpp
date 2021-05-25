#ifndef __IBOOK__
#define __IBOOK__
#include <string>
using namespace std;

class IBook{
    protected:
        string _title;
        string _author;
        int _year;
        string _genre;
    
    public:
        virtual void print() = 0;
};

#endif