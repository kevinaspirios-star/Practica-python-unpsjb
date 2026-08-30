interface Persona {
    nombre:string;
    edad: number;
}

const persona1: Persona= {nombre:"kevin",edad:21};

console.log("Nombre:%s : Edad: %d", persona1.nombre, persona1.edad);