let fecha = new Date("03/23/2026");

let fecha_milisegundos = fecha.getTime();


let dias_cuenta = document.getElementById('dias');
let horas_cuenta = document.getElementById('horas');
let minutos_cuenta = document.getElementById('minutos');
let segundos_cuenta = document.getElementById('segundos');
setInterval(() =>{
    let fecha_actual = new Date().getTime();
    let diferencia = fecha_milisegundos - fecha_actual;

    let dias = Math.floor(diferencia/(1000*60*60*24));
    let horas = Math.floor((diferencia % (1000*60))/(1000*60*60));
    let minutos = Math.floor((diferencia % (1000*60*60))/(1000*60));
    let segundos = Math.floor((diferencia % (1000*60))/1000);

    dias_cuenta.innerText = dias < 10 ? "0" + dias : dias;
    horas_cuenta.innerText = horas < 10 ? "0" + horas : horas;
    minutos_cuenta.innerText = minutos < 10 ? "0" + minutos: minutos;
    segundos_cuenta.innerText = segundos < 10 ? "0" + segundos: segundos;
}, 1000)

function grafico() {
    const contenedor_grafico = document.getElementById('diagrama');
    const data = [
        { mes: 'Ene', value: 45000 },
        { mes: 'Feb', value: 52000 },
        { mes: 'Mar', value: 38000 },
        { mes: 'Abr', value: 65000 },
        { mes: 'May', value: 71000 },
        { mes: 'Jun', value: 89000 },
        { mes: 'Jul', value: 95000 },
        { mes: 'Ago', value: 78000 }
    ];

    const maxValue = Math.max(...data.map(d => d.value));

    data.forEach(item => {
        //Creamos la barra para cada mes
        const bar = document.createElement('div');
        bar.className = 'bar';
        const porcentajeAltura = (item.value / maxValue) * 100;
        bar.style.height = porcentajeAltura + '%';

        //Agregamos la etiqueta del mes
        const label = document.createElement('div');
        label.className = 'bar-label';
        label.textContent = item.mes;

        //Agregamos el valor de la barra
        const value = document.createElement('div');
        value.className = 'bar-value';
        value.textContent = '€' + (item.value / 1000).toFixed(0) + 'K';

        bar.appendChild(label);
        bar.appendChild(value);
        contenedor_grafico.appendChild(bar);
    });
}

window.addEventListener('DOMContentLoaded', () => {
    grafico();
});