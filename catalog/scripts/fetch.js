function setAction(form) {
    const url = "https://publicactiontrigger.azurewebsites.net/api/dispatches/colin-bradshaw-pac/ddf-home";
    const andSign = '&';
    const senderParameter = 'sender='+form.senderEmail.value;      
    const bodyParameter = 'body='+form.senderMessage.value;
    const newUrl = url+senderParameter+andSign+bodyParameter;

    fetch(
        newUrl,
        {            
            headers: { "Content-Type": "application/json" },            
            method: "POST",
            body: ""
        }
        )
    .then(data => data.json())
    .then((json) => {
        alert(JSON.stringify(json));
        document.getElementById("form").reset();     
    });
    return false;
    }