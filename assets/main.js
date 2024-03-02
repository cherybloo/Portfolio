async function get_visitors(url) {
    // call post api request function
    //await post_visitor();
    try {
        let response = await fetch(url, {
            method: 'GET',
        });
        let data = await response.json()
        document.getElementById("visitors").innerHTML = "Thank you for the " + data['visitor'] + " visits";
        console.log(data);
        return data;
    } catch (err) {
        console.error(err);
    }
}


get_visitors('https://i93liv8lga.execute-api.eu-central-1.amazonaws.com/default/VisitorCounter-Lambda');

