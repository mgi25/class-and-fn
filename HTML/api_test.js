const url = "https://api.spaceflightnewsapi.net/v4/articles/"



fetch(url)
    .then(response => response.json())
    .then(data => console.log(data));

    async function getData() {

        try{
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }
            const json = await response.json();
            console.log(json);
            return json;
        } catch (error) {
            console.error(error.message);
        }
    }