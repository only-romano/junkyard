// Механизм наследования очень удобен, но он имеет свои ограничения.  Nнтерфейсы
// определяют некоторый функционал, не имеющий конкретной реализации, который затем
// реализуют классы, применяющие эти интерфейсы. N один класс может применить множество
// интерфейсов. Чтобы определить интерфейс, используется ключевое слово interface.

public interface Printable{

    void print();
}

// Nнтерфейс может определять различные методы, которые, так же как и абстрактные методы
// абстрактных классов не имеют реализации. В данном случае объявлен только один метод.

// Все методы интерфейса не имеют модификаторов доступа, но фактически по умолчанию
// доступ public, так как цель интерфейса - определение функционала для реализации
// его классом. Поэтому весь функционал должен быть открыт для реализации.

// N также при объявлении интерфейса надо учитывать, что только один интерфейс в файле
// может иметь тип доступа public. А его название должно совпадать с именем файла.
// Остальные интерфейсы (если такие имеются в файле java) не должны иметь модификаторов
// доступа.