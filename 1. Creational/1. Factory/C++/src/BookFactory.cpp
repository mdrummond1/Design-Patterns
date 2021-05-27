#include "Books.cpp"

class BookFactory{
    public:
        IBook* CreateBook(string title, string author, int year, BookType type){
            if (type == E_ADVENTURE){
                return new AdventureBook(title, author, year);
            } else if (type == E_DRAMA){
                return new DramaBook(title, author, year);
            } else if (type == E_FANTASY){
                return new FantasyBook(title, author, year);
            }

            return NULL;
        }
};