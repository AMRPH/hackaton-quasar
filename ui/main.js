async function subm(){
    text = document.getElementById("name").value;

    var result = await eel.submit_ans(text)();
    console.log(result);
    var answer = document.getElementById("answer");
    var legal_act = document.getElementById("legal_act");
    var link_ans = document.getElementById("link_ans");


    inner_for_anwser = "Ответ: " + result[0];
    inner_for_legal_act = "НПА: " + result[1];
    inner_for_links = "Ссылка :" + result[2];


    answer.classList.remove("invisible");
    answer.classList.add("visible");
    answer.classList.add("answer");
    answer.innerHTML = inner_for_anwser;


    legal_act.classList.remove("invisible");
    legal_act.classList.add("visible");
    legal_act.classList.add("answer");
    legal_act.innerHTML = inner_for_legal_act;


    link_ans.classList.remove("invisible");
    link_ans.classList.add("visible");
    link_ans.classList.add("answer");
    if (result[2] != "Ссылка не найдена"){  
        document.getElementById("llink").setAttribute('href', result[2]);
        document.getElementById("llink").setAttribute('target', '_blank');
    }
    else{
        document.getElementById("llink").setAttribute('href', '#');
        document.getElementById("llink").setAttribute('target', '_self');
    }
    link_ans.innerHTML = 'Ссылка: <a id = "llink" target="_blank"></a>'
    document.getElementById("llink").innerHTML = result[2]



}