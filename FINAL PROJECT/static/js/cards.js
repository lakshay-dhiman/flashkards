var current_card = 1

var add_card = document.querySelector('#add_card #heading')

if(add_card){
    add_card.addEventListener('click',(e)=>{
        document.querySelector('.form').style.visibility = "visible";
    }) 
    
    document.querySelector('.cross').addEventListener('click',()=>{
        document.querySelector('.form').style.visibility = "hidden";
    })

}




// creation of cards carosel
var next = document.querySelector('#next')
var prev = document.querySelector('#prev')

var card = document.querySelector('.card[data-num = "1"]')

cards =  document.querySelectorAll('.card')

num_cards = cards.length



for(var i =0 ; i < num_cards; i++){
    var elem = document.createElement("div")
    elem.classList.add('dot')
    var target = document.querySelector('#progress');
    target.appendChild(elem)
    console.log('added');
}

if(next){
    next.addEventListener('click',(e)=>{
        // flip all
        var score = document.querySelector(`.card[data-num = "${current_card}"] .score`)
        var card_curr = document.querySelector(`.card[data-num = "${current_card}"]`)
        card_curr.dataset.state = 'front'
        document.querySelector(`.card[data-num = "${current_card}"] .front`).innerHTML = card_curr.dataset.front
        score.style.visibility = 'hidden'

        var next_card = parseInt(card.dataset.num)+1
        if(next_card <= num_cards ){
            card.style.visibility = 'hidden'
            card =  document.querySelector(`.card[data-num = "${next_card}"]`)
            current_card = next_card
            card.style.visibility = 'visible'
        }    
        if(current_card == 1){
            prev.classList.add('deactivate')
        }else{
            prev.classList.remove('deactivate')
        }
    
        if(current_card == num_cards){
            next.classList.add('deactivate')
        }else{
            next.classList.remove('deactivate')
        }
        document.querySelectorAll(`.dot`).forEach(elem =>{
            elem.classList.remove('current')
        })
        document.querySelector(`.dot:nth-child(${current_card})`).classList.add('current')
        //else{
        //     next_card = 1
        //     card.style.visibility = 'hidden'
        //     card =  document.querySelector(`.card[data-num = "${next_card}"]`)
        //     current_card = next_card
        //     card.style.visibility = 'visible'
        // }
    })

    // console.log(current_card);


}


if(prev){
    prev.addEventListener('click',(e)=>{
        // flip all
        var score = document.querySelector(`.card[data-num = "${current_card}"] .score`)
        var card_curr = document.querySelector(`.card[data-num = "${current_card}"]`)
        card_curr.dataset.state = 'front'
        document.querySelector(`.card[data-num = "${current_card}"] .front`).innerHTML = card_curr.dataset.front
        score.style.visibility = 'hidden'

        var prev_card = parseInt(card.dataset.num)-1
        if(prev_card >=1){
            card.style.visibility = 'hidden'
            card =  document.querySelector(`.card[data-num = "${prev_card}"]`)
            current_card = prev_card
            card.style.visibility = 'visible'
        }     
        if(current_card == 1){
            prev.classList.add('deactivate')
        }else{
            prev.classList.remove('deactivate')
        }
    
        if(current_card == num_cards){
            next.classList.add('deactivate')
        }else{
            next.classList.remove('deactivate')
        }
        document.querySelectorAll(`.dot`).forEach(elem =>{
            elem.classList.remove('current')
        })
        document.querySelector(`.dot:nth-child(${current_card})`).classList.add('current')

        // else{
        //     prev_card = num_cards
        //     card.style.visibility = 'hidden'
        //     card =  document.querySelector(`.card[data-num = "${prev_card}"]`)
        //     current_card = prev_card
        //     card.style.visibility = 'visible'
        // }
    })   
    
    // console.log(current_card);

}



cards.forEach(card => {
    card.addEventListener('click',(e)=>{
        var score = document.querySelector(`.card[data-num = "${current_card}"] .score`)
        var card_curr = document.querySelector(`.card[data-num = "${current_card}"]`)
        if (card_curr.dataset.state == 'front'){
            document.querySelector(`.card[data-num = "${current_card}"] .front`).innerHTML = ''
            document.querySelector(`.card[data-num = "${current_card}"] .num`).style.visibility = 'hidden'
            document.querySelector(`.card[data-num = "${current_card}"] .instruction`).style.visibility = 'hidden'

            card_curr.classList.add('rotate')
            setTimeout(() => {
                card_curr.classList.remove('rotate')            
                card_curr.dataset.state = 'back'
                document.querySelector(`.card[data-num = "${current_card}"] .front`).innerHTML = card_curr.dataset.back
                document.querySelector(`.card[data-num = "${current_card}"] .num`).style.visibility = 'visible'
                document.querySelector(`.card[data-num = "${current_card}"] .instruction`).style.visibility = 'visible'
                score.style.visibility = 'visible'
            }, 500);
        }
        else{
            document.querySelector(`.card[data-num = "${current_card}"] .front`).innerHTML = ''
            document.querySelector(`.card[data-num = "${current_card}"] .num`).style.visibility = 'hidden'
            document.querySelector(`.card[data-num = "${current_card}"] .instruction`).style.visibility = 'hidden'
            card_curr.classList.add('rotate')
            score.style.visibility = 'hidden'
            setTimeout(() => {
                card_curr.classList.remove('rotate')            
                card_curr.dataset.state = 'front'
                document.querySelector(`.card[data-num = "${current_card}"] .front`).innerHTML = card_curr.dataset.front
                document.querySelector(`.card[data-num = "${current_card}"] .num`).style.visibility = 'visible'
                document.querySelector(`.card[data-num = "${current_card}"] .instruction`).style.visibility = 'visible'
                score.style.visibility = 'hidden'
            }, 500);
        }
    })    
});


var scores_button = document.querySelectorAll('.score_val')

scores_button.forEach(button => {
    button.addEventListener('click',(e)=>{
        e.stopPropagation();
        if(document.querySelector(`.card[data-num = "${current_card}"]`).dataset.voted != 'true'){
            var score_val = button.dataset.score
            var deck_id = window.location.href.split('/')[window.location.href.split('/').length-1]
            // console.log(deck_id);
            //ajax request
            // var xhttp = new XMLHttpRequest()
            // xhttp.open("POST", "../api/put/review",true)
            // var data = {score : score_val, deck_id : deck_id}
            
            // xhttp.onreadystatechange = function() {
            //     if(xhttp.readyState == 4 && xhttp.status == 200) {
            //         console.log(xhttp.responseText);
            //     }
            // }
            // xhttp.send(data)        

            $.ajax({
                type : 'POST',
                url : '../api/put/review',
                data :{
                    'score' : score_val,
                    'deck_id' : deck_id
                },
                success: (res)=>{
                    // console.log(res);
                    var card_curr = document.querySelector(`.card[data-num = "${current_card}"]`)
                    card_curr.dataset.voted = true
                    button.classList.add('selected')
                    document.querySelectorAll(`.card[data-num = "${current_card}"] button`).forEach((buttonss)=>{
                        buttonss.classList.add('reviewed')
                    })

                }
            })            
        }
    })

});


$("#add_card_form").submit(function(e) {

    e.preventDefault();

    var form = $(this);
    
    $.ajax({
           type: "POST",
           url: '../api/add/card',
           data: form.serialize(), 
           success: function(data){
               if(data == 'success'){
                   window.location.reload()
               }else{
                   alert(data)
               }
           }
         });

    
});

if(next && prev){

    if(current_card == 1){
        prev.classList.add('deactivate')
    }else{
        prev.classList.remove('deactivate')
    }

    if(current_card == num_cards){
        next.classList.add('deactivate')
    }else{
        next.classList.remove('deactivate')
    }
    document.querySelectorAll(`.dot`).forEach(elem =>{
        elem.classList.remove('current')
    })
    document.querySelector(`.dot:nth-child(${current_card})`).classList.add('current')

}