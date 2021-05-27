using System;
namespace MovieFactory
{
    class Program
    {
        static void Main(string[] args)
        {
            var factory = new MovieFactory();
            IMovie sus = factory.GetMovie("Those who wish us dead", 2021, MovieType.Suspense);
            IMovie act = factory.GetMovie("Breach", 2020, MovieType.Action);
            sus.DisplayInfo();
            act.DisplayInfo();
        }
    }
}
