# JavaScript for Django Developers
### DOM Manipulation & Fetch API — Notes for Python Programmers

> You already know Python and programming fundamentals. These notes map that
> knowledge onto JavaScript so you can make your Django templates interactive.

---

## 1. JavaScript vs Python — Quick Orientation

| Concept | Python | JavaScript |
|---|---|---|
| Variable declaration | `x = 5` | `let x = 5;` (or `const x = 5;`) |
| Constant | not built-in (convention `X = 5`) | `const X = 5;` (truly immutable binding) |
| Function | `def greet(name):` | `function greet(name) { }` |
| Print | `print("hi")` | `console.log("hi")` |
| Null/None | `None` | `null` / `undefined` |
| List | `[1, 2, 3]` | `[1, 2, 3]` (Array) |
| Dict | `{"a": 1}` | `{a: 1}` (Object) |
| Equality | `==` (value) | `===` (value **and** type — always prefer this) |
| Comment | `# comment` | `// comment` |
| String interpolation | `f"Hello {name}"` | `` `Hello ${name}` `` (template literals) |
| Blocks | indentation | `{ }` curly braces |

**Rule of thumb:** always use `const` by default, `let` when the variable
changes, and avoid `var` entirely (old, buggy scoping).

```javascript
const name = "Alice";      // won't change
let age = 20;               // will change
age = 21;                   // OK
```

---

## 2. Where Does JavaScript Live in a Django Project?

Just like CSS, JS files go inside your app's `static` folder.

```
myapp/
├── static/
│   └── myapp/
│       ├── style.css
│       └── signup.js
└── templates/
    └── myapp/
        └── signup.html
```

**In your template:**

```django
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'myapp/style.css' %}">
</head>
<body>
    ...
    <!-- Always load JS at the bottom, or use `defer` -->
    <script src="{% static 'myapp/signup.js' %}" defer></script>
</body>
</html>
```

`defer` tells the browser: "load this script in the background, but run it
only after the HTML is fully parsed." Without it, your JS might try to grab
an element that doesn't exist yet.

---

## 3. The DOM (Document Object Model)

Think of the DOM as **the HTML page loaded into memory as a tree of objects**
that JavaScript can read and modify — similar to how `BeautifulSoup` lets
Python read and modify an HTML tree, except this happens live, in the browser.

```
document
 └── html
      ├── head
      └── body
           ├── h1
           └── form
                ├── input
                └── button
```

### 3.1 Selecting Elements

```javascript
// By id  → returns ONE element
const emailInput = document.getElementById("email");

// By CSS selector → returns ONE element (the first match)
const form = document.querySelector("#signup-form");

// By CSS selector → returns ALL matches (a NodeList, like a Python list)
const allInputs = document.querySelectorAll("input");
```

`querySelector` / `querySelectorAll` accept **any CSS selector** — `.class`,
`#id`, `tag`, `[attribute]` — so you rarely need anything else.

### 3.2 Reading & Changing Content

```javascript
const heading = document.querySelector("h1");

heading.textContent;                  // read text (like .text in Python)
heading.textContent = "Welcome!";     // change text

heading.innerHTML = "<b>Welcome!</b>"; // insert HTML (careful: XSS risk)
```

> ⚠️ Prefer `textContent` over `innerHTML` unless you deliberately need to
> insert HTML tags. `innerHTML` can execute injected scripts if the content
> comes from an untrusted source (e.g., user input).

### 3.3 Changing Attributes & Styles

```javascript
const button = document.querySelector("#submit-btn");

button.setAttribute("disabled", "true");
button.removeAttribute("disabled");

button.style.backgroundColor = "green";
button.classList.add("hidden");       // like adding to a set
button.classList.remove("hidden");
button.classList.toggle("active");    // add if absent, remove if present
```

### 3.4 Creating & Inserting Elements

```javascript
const errorMsg = document.createElement("p");   // like list.append() prep
errorMsg.textContent = "Email already taken.";
errorMsg.classList.add("error-text");

form.appendChild(errorMsg);      // insert at the end
form.prepend(errorMsg);          // insert at the beginning
errorMsg.remove();               // delete an element
```

### 3.5 Events

Events are how JS "listens" for user actions — similar to registering a
callback. There's no polling/loop needed; the browser calls your function.

```javascript
button.addEventListener("click", function () {
    console.log("Button clicked!");
});

// Arrow function version (shorter, common in modern JS)
button.addEventListener("click", () => {
    console.log("Button clicked!");
});
```

Common events: `click`, `submit`, `input`, `change`, `keydown`, `mouseover`.

---

## 4. Worked Example: Signup Page (Pure DOM, No Server Yet)

**`signup.html`** (inside a Django template)

```django
{% load static %}
<form id="signup-form">
    <input type="text" id="username" placeholder="Username">
    <input type="email" id="email" placeholder="Email">
    <input type="password" id="password" placeholder="Password">
    <p id="error-msg" class="error-text" style="display:none;"></p>
    <button type="submit" id="submit-btn">Sign Up</button>
</form>

<script src="{% static 'myapp/signup.js' %}" defer></script>
```

**`signup.js`**

```javascript
// 1. Grab elements once, at the top
const form       = document.querySelector("#signup-form");
const username    = document.querySelector("#username");
const email       = document.querySelector("#email");
const password    = document.querySelector("#password");
const errorMsg    = document.querySelector("#error-msg");

// 2. Helper to show an error (like a small utility function in Python)
function showError(message) {
    errorMsg.textContent = message;
    errorMsg.style.display = "block";
}

function clearError() {
    errorMsg.style.display = "none";
}

// 3. Listen for form submission
form.addEventListener("submit", function (event) {
    event.preventDefault();   // stop the browser's default page reload
    clearError();

    if (username.value.trim() === "") {
        showError("Username cannot be empty.");
        return;
    }

    if (!email.value.includes("@")) {
        showError("Enter a valid email.");
        return;
    }

    if (password.value.length < 8) {
        showError("Password must be at least 8 characters.");
        return;
    }

    console.log("Validation passed! Ready to send to server.");
});
```

**Key idea:** `event.preventDefault()` stops the browser's default behavior
(a full page reload on form submit) so we can handle everything with JS —
this is essential before using `fetch`.

---

## 5. The Fetch API — Talking to Your Django Backend

`fetch` is JavaScript's built-in way to make HTTP requests — conceptually
identical to Python's `requests` library.

```python
# Python (requests) — for comparison
import requests
response = requests.post("http://example.com/api/signup/", json={"username": "alice"})
data = response.json()
```

```javascript
// JavaScript (fetch) — equivalent
fetch("/api/signup/", {
    method: "POST",
    body: JSON.stringify({ username: "alice" })
})
    .then(response => response.json())
    .then(data => console.log(data));
```

### 5.1 Promises & async/await

`fetch` returns a **Promise** — an object representing "a value that will
arrive later." You can consume it two ways:

```javascript
// Style A: .then() chains
fetch("/api/data/")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));

// Style B: async/await (cleaner, looks synchronous — PREFERRED)
async function getData() {
    try {
        const response = await fetch("/api/data/");
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error:", error);
    }
}
```

> `async/await` is just syntax sugar over Promises. Think of `await` as
> Python's blocking call — "pause here until this finishes" — except it only
> pauses this function, not the whole browser.

### 5.2 GET Request

```javascript
async function loadUsers() {
    const response = await fetch("/api/users/");   // GET is the default method
    const users = await response.json();
    console.log(users);
}
```

### 5.3 POST Request (Sending Data)

```javascript
async function createUser(username, email) {
    const response = await fetch("/api/signup/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ username: username, email: email }),
    });
    const data = await response.json();
    return data;
}
```

### 5.4 Checking the Response Status

```javascript
const response = await fetch("/api/signup/", { method: "POST", ... });

if (response.ok) {              // true if status is 200-299
    const data = await response.json();
    console.log("Success:", data);
} else {
    console.log("Server error:", response.status);
}
```

---

## 6. CSRF Tokens — The Django-Specific Bit

Django blocks unsafe requests (`POST`, `PUT`, `DELETE`) unless they include a
valid CSRF token. `fetch` does **not** send this automatically like a normal
HTML form does — you must attach it yourself.

**Step 1 — Make sure the token is available in the template:**

```django
{% csrf_token %}
```

This renders a hidden `<input>` with `name="csrftoken"`. Read it in JS:

```javascript
function getCSRFToken() {
    return document.querySelector("[name=csrfmiddlewaretoken]").value;
}
```

**Step 2 — Send it in the request header:**

```javascript
async function createUser(username, email, password) {
    const response = await fetch("/api/signup/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify({ username, email, password }),
    });
    return await response.json();
}
```

> Note: `{ username, email, password }` is **shorthand** for
> `{ username: username, email: email, password: password }` — JS lets you
> drop the key name when it matches the variable name.

---

## 7. Full Example: AJAX Signup (DOM + Fetch Combined)

This is the complete flow: validate in the DOM → send with fetch → update
the DOM with the server's response, **without reloading the page**.

### Django side (`views.py`)

```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
import json

@require_POST
@csrf_protect
def signup_api(request):
    data = json.loads(request.body)
    username = data.get("username")
    email = data.get("email")

    if User.objects.filter(username=username).exists():
        return JsonResponse({"success": False, "error": "Username taken."}, status=400)

    User.objects.create_user(username=username, email=email, password=data.get("password"))
    return JsonResponse({"success": True, "message": "Account created!"})
```

```python
# urls.py
path("api/signup/", views.signup_api, name="signup_api"),
```

### Frontend (`signup.js`)

```javascript
const form     = document.querySelector("#signup-form");
const username = document.querySelector("#username");
const email    = document.querySelector("#email");
const password = document.querySelector("#password");
const errorMsg = document.querySelector("#error-msg");
const submitBtn = document.querySelector("#submit-btn");

function getCSRFToken() {
    return document.querySelector("[name=csrfmiddlewaretoken]").value;
}

function showError(message) {
    errorMsg.textContent = message;
    errorMsg.style.display = "block";
}

function clearError() {
    errorMsg.style.display = "none";
}

async function submitSignup(data) {
    const response = await fetch("/api/signup/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify(data),
    });
    return { ok: response.ok, data: await response.json() };
}

form.addEventListener("submit", async function (event) {
    event.preventDefault();
    clearError();

    // --- Client-side validation (fast feedback, no server round-trip) ---
    if (username.value.trim() === "") return showError("Username required.");
    if (!email.value.includes("@")) return showError("Valid email required.");
    if (password.value.length < 8) return showError("Password too short.");

    // --- Disable button while request is in-flight ---
    submitBtn.disabled = true;
    submitBtn.textContent = "Creating account...";

    // --- Talk to Django ---
    const { ok, data } = await submitSignup({
        username: username.value,
        email: email.value,
        password: password.value,
    });

    submitBtn.disabled = false;
    submitBtn.textContent = "Sign Up";

    // --- Update the DOM based on server response ---
    if (ok) {
        form.innerHTML = `<p class="success-text">${data.message}</p>`;
    } else {
        showError(data.error);
    }
});
```

**What happens, step by step:**
1. User clicks submit → `preventDefault()` stops the page reload.
2. JS validates fields locally (instant feedback, saves a server call).
3. `fetch` sends a `POST` with JSON body + CSRF token in headers.
4. Django validates again (never trust the client!) and returns JSON.
5. JS reads `response.json()` and updates the DOM — replacing the form with
   a success message, or showing the server's error — all without a full
   page reload.

---

## 8. Cheat Sheet

```javascript
// SELECT
document.querySelector("#id");
document.querySelectorAll(".class");

// READ / WRITE CONTENT
el.textContent;
el.textContent = "new text";

// ATTRIBUTES & CLASSES
el.setAttribute("disabled", "true");
el.classList.add("hidden");
el.classList.toggle("active");

// CREATE / REMOVE
const p = document.createElement("p");
parent.appendChild(p);
el.remove();

// EVENTS
el.addEventListener("click", (event) => { });
event.preventDefault();

// FETCH — GET
const res = await fetch("/api/data/");
const data = await res.json();

// FETCH — POST (Django, CSRF required)
await fetch("/api/endpoint/", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(),
    },
    body: JSON.stringify({ key: "value" }),
});
```

---

## 9. Common Mistakes to Avoid

| Mistake | Fix |
|---|---|
| Script runs before HTML loads → `null` errors | Use `defer` on `<script>`, or place script at end of `<body>` |
| Form still reloads the page | Call `event.preventDefault()` inside the submit handler |
| `403 Forbidden` on POST requests | Send the `X-CSRFToken` header (see Section 6) |
| Forgetting `Content-Type: application/json` | Django's `request.body` won't parse correctly without it |
| Using `innerHTML` with user input | Use `textContent` to avoid script-injection risk |
| Comparing with `==` | Always use `===` in JavaScript |
| Not `await`-ing `response.json()` | It's async — always `await` it (or chain `.then()`) |

---

## 10. Summary

- The **DOM** is your live HTML tree — `document.querySelector` to find
  elements, then read/write `textContent`, attributes, classes, or create
  new elements entirely.
- **Events** (`addEventListener`) let JS react to user actions instead of
  polling for them.
- **`fetch`** is JS's `requests` equivalent — always paired with
  `async/await` for readable code.
- In Django, remember: **CSRF token in the header**, **`JsonResponse`** on
  the server, **`response.json()`** on the client.
- Combine all three (DOM + events + fetch) to build interactive pages, like
  the signup form above, that talk to Django **without full page reloads**.
