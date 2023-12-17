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
    urls = result[2].split(' ');
    link_ans.innerHTML = 'Ссылка: ';

    for (let i = 0; i < urls.length; i++) {
        link_ans.innerHTML += '<a class = "llink" target="_blank" href="'+urls[i]+'">'+urls[i]+'</a></br>'
    }
    
    if (result[2] == "Ссылка не найдена"){
        link_ans.innerHTML ='Ссылка: Ссылка не найдена';
    }




}