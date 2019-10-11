// Nнтерфейсы в механизме обратного вызова

public class EventsApp  {

    public static void main(String[] args) {

        Button button = new Button(new ButtonClickHandler());
        button.click();
        button.click();
        button.click();

        Button tvButton = new Button(new EventHandler(){

            private boolean on = false;
            public void execute(){

                if(on) {
                    System.out.println("Телевизор выключен..");
                    on=false;
                }
                else {
                    System.out.println("Телевизор включен!");
                    on = true;
                }
            }
        });

        Button printButton = new Button(new EventHandler() {

            public void execute(){

                System.out.println("Запущена печать на принтере..");
            }
        });

        tvButton.click();
        printButton.click();
        tvButton.click();
    }
}

class ButtonClickHandler implements EventHandler{

    public void execute(){

        System.out.println("Кнопка нажата!");
    }
}

interface EventHandler{

    void execute();
}

class Button{

    EventHandler handler;
    Button(EventHandler action){

        this.handler=action;
    }
    public void click(){

        handler.execute();
    }
}

// На момент определения класса нам не всегда бывают точно известны те
// действия, которые должны производиться. Особенно если класс Button и
// класс основной программы находятся в разных пакетах, библиотеках и могут
// проектироваться разными разработчиками. К тому же у нас может быть
// несколько кнопок - объектов Button и для каждого объекта надо определить
// свое действие.