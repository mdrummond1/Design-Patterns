#include <iostream>
#include "./src/BookFactory.cpp"

int main(int, char**) {

    BookFactory factory = BookFactory();
    IBook* dram = factory.CreateBook("Charlie's Chance", "M.L. Nesbitt", 1868, E_DRAMA);
    dram->print();
    
    IBook* adv = factory.CreateBook("Swiss Family Robinson", "Johann David Wyss", 1812, E_ADVENTURE);
    adv->print();

    IBook* fant = factory.CreateBook("the Lord of the Rings", "J.R.R. Tolkien", 1954, E_FANTASY);
    fant->print();
    return 0;
}