document.getElementById("quizForm").addEventListener("submit", async function(e){

e.preventDefault();

let answers=[];

for(let i=0;i<12;i++){

    let answer=document.querySelector(`input[name="q${i}"]:checked`);

    if(!answer){
        alert("Please answer all questions.");
        return;
    }

    answers.push(answer.value);
}

const response=await fetch("/result",{
    method:"POST",
    headers:{
        "Content-Type":"application/json"
    },
    body:JSON.stringify(answers)
});

const data=await response.json();

localStorage.setItem("result",JSON.stringify(data));

window.location="/show_result";


});

