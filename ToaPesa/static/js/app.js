
const numberID = document.getElementById('number');
const amountID = document.getElementById('amount');
const agentID = document.getElementById('agentID');
//const passwordID = document.getElementById('password');

function show(id, value) {
    document.getElementById(id).style.display = value ? 'block' : 'none';
}

function withdraw() {
    if((numberID.value).substring(0, 2) == "07" && (numberID.value).length == 10){
        if(amountID.value >= 100){
            var number0 = numberID.value;
            var amountEntred = parseInt(amountID.value);
            var amount;
            var agent = agentID.value;
            var number = '255' + number0.substring(1);

            if(100 <= amountEntred && amountEntred <= 999){
                amount = amountEntred + 100;
            }
            if(1000 <= amountEntred && amountEntred <= 2999){
                amount = amountEntred + 170;
            }
            if(3000 <= amountEntred && amountEntred <= 4999){
                amount = amountEntred + 307;
            }
            if(5000 <= amountEntred && amountEntred <= 9999){
                amount = amountEntred + 400;
            }
            if(10000 <= amountEntred && amountEntred <= 29999){
                amount = amountEntred + 500;
            }
            if(30000 <= amountEntred && amountEntred <= 49999){
                amount = amountEntred + 1000;
            }
            if(50000 <= amountEntred && amountEntred <= 99999){
                amount = amountEntred + 900;
            }
            if(100000 <= amountEntred && amountEntred <= 199999){
                amount = amountEntred + 1000;
            }
            if(200000 <= amountEntred && amountEntred <= 299999){
                amount = amountEntred + 1500;
            }
            if(300000 <= amountEntred && amountEntred <= 399999){
                amount = amountEntred + 2000;
            }
            if(400000 <= amountEntred && amountEntred <= 499999){
                amount = amountEntred + 2900;
            }
            if(500000 <= amountEntred && amountEntred <= 799999){
                amount = amountEntred + 4000;
            }
            if(800000 <= amountEntred && amountEntred <= 999999){
                amount = amountEntred + 4000;
            }
            if(1000000 <= amountEntred && amountEntred <= 3000000){
                amount = amountEntred + 3100;
            }
            if(amountEntred > 3000000){
                amount = amountEntred + 5000;
            }
            
            swal("Please wait ...")
            //apiSandBox
            //openAPI
            var data = number+"="+amount+"="+agent;
            $.ajax({
                type:'POST',
                url: "/openAPI/"+data
            }).done(function(res) {
                console.log(res);
                if(res.code == 200){
                    var sessionID = res.sessionID;
                    swal({
                        title: "success",
                        text: "Mtaarifu mteja aangalie simu yake ili aweke namba ya siri",
                        icon: "success",
                    });
                    sendSessionID(sessionID,data);
                    console.log(sessionID);
                    console.log(data);

                }else{
                    //text: res.code+" error : "+(res.body).output_ResponseDesc,
                    swal({
                        title: "Mtandao haujafanikiwa",
                        text: "Mteja hataweza kupata message ya PIN",
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



function sendSessionID(mSessionID,mdata){
    show('loading', true);
    var refreshIntervalId = setInterval(function () {swal.close()}, 5000);
    var data = mdata+"="+mSessionID;
        $.ajax({
                type:'POST',
                url: "/openAPIResult/"+data
        }).done(function(res) {
            //console.log(res);
            clearInterval(refreshIntervalId);
            if(res.code == 201){
                show('loading', false);
                swal({
                    title: "Congrants",
                    text: "Umefanikiwa kutoa hela",
                    icon: "success",
                });
                sendSMS(res.number,res.head,res.message)
            }else{
                show('loading', false);
                swal({
                    title: "Muamala haujafanikiwa",
                    text: res.code+" error : "+(res.body).output_ResponseDesc,
                    icon: "error",
                }); 
            }
    });
}





function sendSMS(phone,head,body){
    var data = phone+"="+head+"="+body;
        $.ajax({
                type:'POST',
                url: "/notifications/"+data
        }).done(function(res) {
            //console.log(res);
            if(res.code == 201){
                swal({
                    title: "Hongera",
                    text: "Message Imethibitishwa amefanikiwa kutoa hela",
                    icon: "success",
                });
            }else{
                swal({
                    title: "Message fails",
                    text: "Message hazijatumwa kwa mteja muulize akuoneshe message ya malipo",
                    icon: "error",
                }); 
            }
    });
}







