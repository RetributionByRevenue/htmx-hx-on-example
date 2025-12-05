from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi import HTTPException

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
</head>
<body>

<form
    hx-post="/submit"
    hx-target="#result"
    hx-swap="innerHTML"

    hx-on="
        htmx:beforeRequest: console.log('Making a request!')
        htmx:responseError: console.log('catching error!')
        htmx:afterRequest: (function() {
                                if (event.detail.xhr.status === 200) {
                                    console.log('was successful')
                                } 
                                else if(event.detail.xhr.status === 204) {
                                    console.log('successful, no content to be returned!')
                                }
                                $('.my-box').remove()
                            })()
    "
>
    <label>Email:</label>
    <input 
        type="text" 
        name="email"
    >
    <button type="submit">Submit</button>
</form>

<div id="result"></div>

</body>
</html>
    """

@app.post("/submit", response_class=HTMLResponse)
async def submit(email: str = Form(...)):
    if not email.endswith("@example.com"):
        raise HTTPException(status_code=400, detail="Invalid email — must end with @example.com")

    return f"<p>Success! Email: {email}</p>"
