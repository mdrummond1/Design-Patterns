using System;

namespace MovieFactory {
    public enum MovieType{
        Action,
        Suspense
    };
    
    public class Movie : IMovie{
        public string Title;
        public int Year;
        public string Genre;
        public Movie(string title, int year, string genre){
            Title = title;
            Year = year;
            Genre = genre;
        }

        public void DisplayInfo(){
            Console.WriteLine($"the {Genre} movie, {Title} was made in {Year}.");
        }
    }

    public class ActionMovie: Movie{
        public ActionMovie(string title, int year)
            : base(title, year, "Action"){}

    }

    public class SuspenseMovie: Movie{
        public SuspenseMovie(string title, int year)
            : base(title, year, "Suspense"){}
    }
    
}