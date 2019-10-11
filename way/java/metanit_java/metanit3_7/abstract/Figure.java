// Другим хрестоматийным примером является системы фигур.  В реальности не
// существует геометрической фигуры как таковой.  Есть круг, прямоугольник,
// квадрат, но просто фигуры нет.  Однако же и круг, и прямоугольник имеют
// что-то общее и являются фигурами:

public abstract class Figure{

    float x; // x-координата точки
    float y; // y-координата точки

    public Figure(float x, float y){

        this.x=x;
        this.y=y;
    }

    public abstract float getPerimeter();
    public abstract float getArea();
}

class Rectangle extends Figure
{
    private float width;
    private float height;

    public Rectangle(float x, float y, float width, float height){

        super(x,y);
        this.width = width;
        this.height = height;
    }

    public float getPerimeter(){

        return width * 2 + height * 2;
    }

    public float getArea(){

        return width * height;
    }
}