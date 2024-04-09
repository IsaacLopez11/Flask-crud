import axios from "axios";

async function hello() {
    await axios.get('http://127.0.0.1:5000/hola')
        .then(response => {
            console.log(response);
        })
        .catch(error => {
            console.error(error);
        });
}

console.log("hola")
hello()
