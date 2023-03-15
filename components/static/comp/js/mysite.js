window.addEventListener('click', function(e){   
    if (!document.getElementById("toggle").contains(e.target)){
        $(".active").removeClass("active");
    }
    if (!document.getElementById("tec-toggle").contains(e.target)){
        $(".tec-active").removeClass("tec-active");
    }
    if (!document.getElementById("pro-toggle").contains(e.target)){
        $(".pro-active").removeClass("pro-active");
    }
    if (!document.getElementById("menutap").contains(e.target)){
        $(".navmenu-active").removeClass("navmenu-active");
    }
});

// var counter = 1;
// setInterval(() => {
//     document.getElementById("radio"+counter).checked = true;
//     counter++;
//     if(counter>4){
//         counter=1;
//     }
// }, 5000);

// $(".buynow").click(function(){
//     var id = $(this).attr("pid").toString();
//     var quan = document.getElementById("quan").innerText;
//     $.ajax({
//         type : "GET",
//         url : "/buy-now/",
//         dara : {
//             'prod_id' : id,
//         },
//         success:function(data){
//             console.log("yes");
//         }
//     })
// });

$('.cart-plus').click(function(){
    var id = $(this).attr("pid").toString();
    $.ajax({
        type : "GET",
        url:"/pluscart",
        data:{
            prod_id : id
        },
        success:function(data){
            document.getElementById(id).innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("total_amount").innerText = data.total_amount
        }
    })
});

$(".cart-minus").click(function(){
    var id = $(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url : "/minuscart",
        data:{
            prod_id : id
        },
        success:function(data){
            document.getElementById(id).innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("total_amount").innerText = data.total_amount
        }
    })
});
// $('.remove').click(function(){
//     var id = $(this).attr("pid").toString();
//     $.ajax({
//         type : "GET",
//         url : "/delete-cart",
//         data : {
//             prod_id : id
//         },
//         success:function(){
//             window.location('components:carts')
//             console.log('success')
//         }
//     })
// });

var q = document.getElementById("quan").innerText;
q = parseInt(q);
$('.cart-dminus').click(function(){
    if(q > 1){
        q -= 1;
    }
    $.ajax({
        type:"GET",
        url : "/prodminus",
        data:{
            q : q
        },
        success:function(data){
            document.getElementById("quan").innerText = data.quan;
        }
    })
});

$('.cart-dplus').click(function(){
    q += 1;
    $.ajax({
        type:"GET",
        url : "/prodplus",
        data:{
            q : q
        },
        success:function(data){
            document.getElementById("quan").innerText = data.quan;
        }
    })
});


function fashionDropDown(){
    $(".dropdown").toggleClass("active");
};

function tecDropDown(){
    $(".tec-dropdown").toggleClass("tec-active");
};
function proDropDown(){
    $(".pro-dropdown").toggleClass("pro-active");
};

function tapDropDown(){
    $(".nav-menu").toggleClass("navmenu-active");
};
