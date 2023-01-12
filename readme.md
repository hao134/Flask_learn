# Note
1. start: Serving HTML files : https://youtube.com/watch?v=QrK50lIwgbk&feature=shares
2. Serving static files with Flask : https://youtube.com/watch?v=GxT0zgZSHE8&feature=shares
3. Flask HTML templates with Jinja: https://youtube.com/watch?v=pj1iLRljwxI&feature=shares
4. Working with Jinja templates : https://youtube.com/watch?v=mqrbF0qGSLI&feature=shares
5. Forms with Flask : https://youtube.com/watch?v=ap2vxzAZVIg&feature=shares
6. Dynamic URL's with Flask : https://youtube.com/watch?v=HgPX3Ix65nE&feature=shares
7. FLASK WITH JSON : https://youtube.com/watch?v=VzBtoA_8qm4&feature=shares
8. Flask & the Fetch API (AJAX?): https://youtube.com/watch?v=QKcVjdLEX_s&feature=shares
創立一個guest_book網頁(1)，將訊息輸入並submit訊息到endpoint(/guestbook/create-entry)，並且此endpoint接收到以後會回傳訊息(2)，回傳訊息後被前端網頁(guestbook.html)接住並且console出來(3)
* what's new ?
1. at views.py, add:
```
#(1)
@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()
    print(req)
    #(2)
    res = make_response(jsonify(req),200)

    return res
```
2. at guestbook.html:
```
{% block script %}
<script>
    function submit_entry() {
        var name = document.getElementById("name");
        var message = document.getElementById("message");

        var entry = {
            name: name.value,
            message: message.value
        };

        //(3)
        fetch(`${window.origin}/guestbook/create-entry`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(entry),
            cache: "no-cache",
            headers: new Headers({
                "content-type":"application/json"
            })
        })
        .then(function (response) {
            if (response.status !== 200) {
                console.log(`Response status was not 200: ${response.status}`);
                return ;
            }

            response.json().then(function (data){
                console.log(data)
            })
        })
    }
</script>
{% endblock %}
```
9. Flask query strings : https://youtube.com/watch?v=PL6wzmKrgRg&feature=shares
10. Flask app configuration : https://youtube.com/watch?v=GW_2O9CrnSU&feature=shares
11. Uploading files with Flask : https://youtube.com/watch?v=6WruncSoCdI&feature=shares
