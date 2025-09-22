class Shape {
    getArea() {
        return 0;   // base class gives no real area
    }
}

class Circle extends Shape {
    constructor(r) {
        super();
        this.r = r;
    }
    getArea() {
        return Math.PI * this.r * this.r;
    }
}

class Triangle extends Shape {
    constructor(base, height) {
        super();
        this.base = base;
        this.height = height;
    }
    getArea() {
        return 0.5 * this.base * this.height;
    }
}

// Checking
let c = new Circle(7);
console.log("Circle area:", c.getArea().toFixed(2));

let t = new Triangle(12, 6);
console.log("Triangle area:", t.getArea());
