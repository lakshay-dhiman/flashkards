var add_deck = document.querySelector('#add')

add_deck.addEventListener('click',(e)=>{
    document.querySelector('#addForm').style.visibility = "visible";
})

document.querySelector('.cross').addEventListener('click',(e)=>{
    e.stopPropagation();
    document.querySelector('#addForm').style.visibility = "hidden"; 
    // console.log('working');
})

var delete_deck = document.querySelectorAll('.delete')
delete_deck.forEach((elem)=>{
    elem.addEventListener('click', ()=>{
        var opt = window.confirm("are you sure you want to delete this deck")

        if(opt){
            deck_id = elem.dataset.deckid
            user_id = elem.dataset.userid
            $.ajax({
                type : 'delete',
                url : '../api/delete/deck',
                data :{
                    'deck_id' : deck_id,
                    'user_id' : user_id
                },
                success: (res)=>{
                    if(res = 'success'){
                        window.location.reload()    
                    }else{
                        alert(res)
                    }
                    
                }
            })             
        }

    })    
})


$("#add_deck_form").submit(function(e) {

    e.preventDefault();

    var form = $(this);
    var url = form.attr('action');
    
    $.ajax({
           type: "POST",
           url: '../api/add/deck',
           data: form.serialize(), 
           success: function(data)
           {
               if(data == 'success'){
                   window.location.reload()
               }else{
                   alert(data)
               }
           }
         });

    
});