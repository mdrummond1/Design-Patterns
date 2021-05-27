using System;
namespace FurnitureAbstractFactory{
    public class Chair: IFurniture{
        private string _type;
        public Chair(string type){
            _type = type;
        }
        public override void print(){
            Console.WriteLine($"This is a {_type} chair");
        }
    }

    
}