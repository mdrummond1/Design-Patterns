#include <iostream>
#include "../include/IBook.hpp"
using namespace std;

enum BookType{
    E_FANTASY,
    E_DRAMA,
    E_ADVENTURE
};

class Book: public IBook{
    protected:
        Book(string title, string author, int year, string genre){
            _title = title;
            _author = author;
            _year = year;
            _genre = genre;
        }

        void print(){
            cout << _genre << " book " << _title << " written in " << _year << " by " << _author << endl;
        }
};

class FantasyBook: public Book{
    public:
        FantasyBook(string title, string author, int year)
            : Book(title, author, year, "fantasy") {}
};

class DramaBook: public Book{
    public:
        DramaBook(string title, string author, int year)
            : Book(title, author, year, "drama"){}
};

class AdventureBook: public Book{
    public:
        AdventureBook(string title, string author, int year)
            : Book(title, author, year, "adventure"){}
};
