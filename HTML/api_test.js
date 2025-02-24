const url = "https://api.spaceflightnewsapi.net/v4/articles/"



fetch(url)
    .then(response => response.json())
    .then(data => console.log(data));
