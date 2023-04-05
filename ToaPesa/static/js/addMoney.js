
const numberID = document.getElementById('number');
const amountID = document.getElementById('amount');
const agentID = document.getElementById('agentID');
//const passwordID = document.getElementById('password');

function godeposit(){
    window.location.replace("url_for('addmoney')");
}

function deposit() {
    if((numberID.value).substring(0, 2) == "07" && (numberID.value).length == 10){
        if(amountID.value >= 100){
            var number0 = numberID.value;
            var amountEntred = parseInt(amountID.value);
            var amount = amountID.value;
            var agent = agentID.value;
            var number = '255' + number0.substring(1);
            //console.log(number)
            swal("Please wait ...")
            //apiSandBox
            //openAPI
            var data = number+"="+amount+"="+agent;
            $.ajax({
                type:'POST',
                url: "/openAPIDeposit/"+data
            }).done(function(res) {
                console.log(res);
                if(res.code == 201){
                    swal({
                        title: "Congrants",
                        text: "Umefanikiwa kuweka hela",
                        icon: "success",
                    });
                }else{
                    swal({
                        title: "Muamala haujafanikiwa",
                        text: res.code+" error : "+(res.body).output_ResponseDesc,
                        icon: "error",
                    }); 
                }
            });

        }else{
            swal({
                title: "Kiasi sio sahihi",
                text: "Weka kiasi kuanzia Tsh 100",
                icon: "error",
            });
        }

    }else{
        swal({
            title: "Namba sio sahihi",
            text: "Weka namba ya vodacom MPESA mfano 0755443322",
            icon: "error",
        });
    }
}