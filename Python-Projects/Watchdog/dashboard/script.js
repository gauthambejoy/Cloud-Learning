console.log("Script loaded");

function statusUpdate() {
    const statusDisplay = document.getElementById("dashboard-status")
    fetch("/api/status")
        .then(response =>{

            if(!response.ok){
                throw new Error("Could not fetch resource")
            }
            return response.json();
        })
        .then(data => {
            statusDisplay.textContent = `Backend: ${data.REDIS}`;
            if (data.REDIS == "Connected"){
                statusDisplay.style.color = "green";
            } else {
                statusDisplay.style.color = "red";
            }      
            console.log(data.REDIS);
        })
        .catch(error =>{
            statusDisplay.textContent = `Error: ${error.message}`;
            statusDisplay.style.color = "red";
            console.error(error)
        });
}
statusUpdate()

function metricsUpdate() {
    const cpuMetrics = document.getElementById("cpu-metrics")
    const memMetrics = document.getElementById("mem-metrics")
    const disMetrics = document.getElementById("disk-metrics")
    fetch("/api/metrics")
        .then(response =>{
            if(!response.ok){
                throw new Error("Could not load resource")
            }
            return response.json();
        })
        .then(data =>{
            cpuMetrics.textContent = `${data.CPU}`;
            console.log(data.CPU);
            memMetrics.textContent = `${data.MEMORY}`;
            console.log(data.MEMORY);
            disMetrics.textContent = `${data.DISK}`;
            console.log(data.DISK);

            cpuMetrics.style.color = "";
            memMetrics.style.color = "";
            disMetrics.style.color = "";
        })
        .catch(error =>{
            cpuMetrics.textContent = `Error: ${error.message}`;
            cpuMetrics.style.color = "red";
            memMetrics.textContent = `Error: ${error.message}`;
            memMetrics.style.color = "red";
            disMetrics.textContent = `Error: ${error.message}`;
            disMetrics.style.color = "red";
            console.error(error)
        })
}
metricsUpdate()


setInterval(metricsUpdate, 10000)
setInterval(statusUpdate, 1000)

function lastUpdated() {
    const date = new Date;
    document.getElementById("last-update").innerHTML = date.toLocaleTimeString()
}

setInterval(lastUpdated, 10000)