//no URL iegūst vārdu un ievieto to virsrakstā
let adrese = window.location.hash;
adrese = decodeURI(adrese);
adrese = adrese.replace('#','');
adrese = adrese.split(",");
vards  = adrese[0];
klikski = adrese[1];
laiks = adrese[2];

let datums = new Date();
let datumsVirkne = datums.getDate()+'.'+datums.getMonth()+'.'+datums.getFullYear()+'.'

async function iegutDatusNoApi(url)
{
  let response = await fetch(url);
  if(!response.ok) {
    throw new Error('HTPP kļūda! Statuss: ${response.status}' );
  }
  return await response.json();
}

async function atlasitTop()
{
  try {
    let topsJson = await iegutDatusNoApi('/topData');
    console.log("Top dati:", topsJson);
    let tabula = document.querySelector(".tops");
    topsJson.forEach(ieraksts => {
    tabula.innerHTML += `
    <tr>
    <td>${ieraksts.vards}</td>
    <td>${ieraksts.klikski}</td>
    <td>${ieraksts.laiks}</td>
    <td>${ieraksts.datums} </td>
    </tr>`;
    });
} catch (e) {console.error("Kļūda, iegūstot top datus", e);
}
}

atlasitTop();

function pievienotTop() {
  let tabula = documen.querySelector('.tops');
  tabula.innerHTML = tabula.innerHTML +`
  <tr id='jauns'>
  <td> `+vards+`</td>
  <td> `+klikski+`</td>
  <td> `+laiks+`</td>
  <tr> `+datumsVirkne+`</tr>`
}
