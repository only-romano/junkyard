package metanit;

public class Metanit3_3{

    public static void main(String[] args){

        // Все члены класса в языке Java - поля и методы, свойства - имеют
        // модификаторы доступа.  В прошлых темах мы уже сталкивались с
        // модификатором public.  Модификаторы доступа позволяют задать
        // допустимую область видимости для членов класса, то есть контекст,
        // в котором можно употреблять данную переменную или метод.

        // В Java используются следующие модификаторы доступа:
        //  .. public: публичный, общедоступный класс или член класса.
        //             Поля и методы, объявленные с модификатором public,
        //             видны другим классам из текущего пакета и из внешних
        //             пакетов.
        //  .. private: закрытый класс или член класса, противоположность
        //             модификатору public.  Закрытый класс или член класса
        //             доступен только из кода в том же классе.
        //  .. protected: такой класс или член класса доступен из любого
        //             места в текущем классе или пакете или в производных
        //             классах, даже если они находятся в других пакетах.
        //  .. Модификатор по умолчанию.  Отсутствие модификатора у поля
        //             или метода класса предполагает применение к нему
        //             модификатора по умолчанию.  Такие поля или методы
        //             видны всем классам в текущем пакете.

        // Казалось бы, почему бы не объявить все переменные и методы с
        // модификатором public?  Однако использование различных
        // модификаторов гарантирует, что данные не будут искажены или
        // изменены не надлежащим образом.  Подобное сокрытие данных
        // называется инкапсуляцией.

        // А вместо непосредственного использования полей, как правило,
        // используют методы доступа:
        }

        private String name;

        public void setName(String name){

            this.name = name;
        }

        public String getName(){

            return name;
    }
}