// Ранее до JDK 8 при реализации интерфейса мы должны были обязательно реализовать
// все его методы в классе. А сам интерфейс мог содерать только определения методов
// без конкретной реализации. В JDK 8 была добавлена такая функциональность как методы
// по умолчанию. Tеперь интерфейсы кроме определения методов могут иметь их реализацию
// по умолчанию, которая используется, если класс, реализующий данный интерфейс, не
// реализует метод. Например, создадим метод по умолчанию в интерфейсе Printable:

interface Printable2 {

    default void print(){

        System.out.println("Неизвестное печатное издание");
    }
}

// Метод по умолчанию - это обычный метод без модификаторов, который помечается
// ключевым словом default. Затем в классе Journal2 нам необязательно этот метод
// реализовать, хотя мы можем его и переопределить.