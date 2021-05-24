namespace MovieFactory{
    public interface IMovieFactory{
        public IMovie GetMovie(string title, int year, MovieType type);
    }
}