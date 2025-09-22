class University {
    constructor(universityName) {
        this.universityName = universityName;
        this.departments = [];
    }

    addDept(name) {
        this.departments.push(name);
        console.log(`Department '${name}' added.`);
    }

    removeDept(name) {
        this.departments = this.departments.filter(d => d !== name);
        console.log(`Department '${name}' removed if it existed.`);
    }

    listDepts() {
        console.log(`Departments in ${this.universityName}:`);
        this.departments.forEach(d => console.log(" - " + d));
    }
}

// Example
let myUni = new University("Tech University");
myUni.addDept("Computer Science");
myUni.addDept("Physics");
myUni.listDepts();
myUni.removeDept("Physics");
myUni.listDepts();
