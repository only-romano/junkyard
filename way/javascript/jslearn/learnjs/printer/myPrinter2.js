const createPrinter = () => {
    const name = "King";

    const printName = () => {
        return name;
    }

    return printName;
}

const myPrinter = createPrinter();

alert(myPrinter());