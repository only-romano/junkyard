package metanit.pak1;

import metanit.pak1.ClassA;     // Ясно

public class ClassB{

    public void result(){

        ClassA classA = new ClassA();
        // System.out.println(classA.num1);  // ошибка, так как num1 - private
        classA.displayNum1();  // public

        System.out.println(classA.num2);  // идентификатор по умолчанию
        classA.displayNum2();  // protected

        System.out.println(classA.num3);  // protected
        classA.displayNum3();  // идентификатор по умолчанию

        System.out.println(classA.num4);  // public
        // classA.displayNum4();  // ошибка, так как private
    }
}