# htmx-hx-on-example
hx-on attribute to manage events before and after a swap


```
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
```
