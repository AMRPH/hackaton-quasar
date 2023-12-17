async function subm(){
    text = document.getElementById("name").value;

    let result = await eel.submit_ans(text)();
    console.log(result);
    document.getElementById("answer").innerHTML = "Ответ: " + result[0];
    document.getElementById("legal_act").innerHTML = "НПА: " + result[1];
    document.getElementById("link_ans").innerHTML = "Ссылка :" + result[2];
    document.getElementById("answer").classList.add('answer');
    document.getElementById("legal_act").classList.add('answer');
    document.getElementById("link_ans").classList.add('answer');
}