namespace MovieFactory{
    public class MovieFactory : IMovieFactory{
        public IMovie GetMovie(string title, int year, MovieType type){
                if (type == MovieType.Action)
                    return new ActionMovie(title, year);
                else if (type == MovieType.Suspense)
                    return new SuspenseMovie(title, year);

                return null;
            }
    }
}