package metanit.pak2;

import metanit.pak1.ClassA;

public class ClassC{

    public void result(){

        ClassA classA = new ClassA();
        // System.out.println(classA.num1);  // ошибка - private
        classA.displayNum1();  // public

        // System.out.println(classA.num2);  // ошибка так как num2 - по умолч
        // classA.displayNum2();  // ошибка, так как protected

        // System.out.println(classA.num3);  // ошибка, так как protected
        // classA.displayNum3();  // ошибка, так как по умолчанию

        System.out.println(classA.num4);  // public
        // classA.displayNum4();  // ошибка, так как private
    }
}