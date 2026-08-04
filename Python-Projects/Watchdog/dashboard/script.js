console.log("Script loaded");
fetch("http://100.94.107.43/api/status")
    .then(response =>{

        if(!response.ok){
            throw new Error("Could not fetch resource")
        }
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error(error))