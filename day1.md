
# 🌐 Introduction to HTML

**HTML (HyperText Markup Language)** is the standard language used to create and design web pages. It structures the content using various tags and elements.

---

## 🔹 HTML Elements

An **HTML element** consists of a start tag, content, and an end tag:

```html
<p>This is a paragraph.</p>
```

Elements can be **nested** inside each other.

---

## 🔸 HTML Attributes

Attributes provide **additional information** about elements. They're always defined in the **start tag**.

```html
<img src="logo.png" alt="Company Logo" width="100" height="100">
```

Common attributes include `id`, `class`, `href`, `src`, `alt`, and `style`.

---

## 🧩 Document Structure

A basic HTML5 document structure looks like this:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Page</title>
</head>
<body>
  <h1>Hello, World!</h1>
</body>
</html>
```

* `<!DOCTYPE html>` declares HTML5
* `<html>` is the root element
* `<head>` contains metadata
* `<body>` contains visible content

---

## 💬 HTML Comments

Used to add notes in code, ignored by browsers.

```html
<!-- This is a comment -->
```

---

## 🔠 HTML Headings

Defined using `<h1>` to `<h6>`:

```html
<h1>Main Heading</h1>
<h2>Subheading</h2>
```

`<h1>` is the most important, `<h6>` the least.

---

## 📝 HTML Paragraphs

Use the `<p>` tag:

```html
<p>This is a paragraph of text.</p>
```

---

## 🔗 HTML Links

Created with the `<a>` tag and `href` attribute:

```html
<a href="https://example.com">Visit Example</a>
```

---

## 🖼️ HTML Images

Use the `<img>` tag, which is **self-closing**:

```html
<img src="image.jpg" alt="A sample image">
```

---

## 🌟 Favicon

A **favicon** is the small icon shown in browser tabs. Defined in the `<head>`:

```html
<link rel="icon" href="favicon.ico" type="image/x-icon">
```

---

## 🏷️ Page Title

Set using the `<title>` tag inside `<head>`:

```html
<title>My Web Page</title>
```

---

## 📊 Tables

Defined with `<table>`, and use:

* `<tr>` for rows
* `<th>` for headers
* `<td>` for data

```html
<table>
  <tr>
    <th>Name</th><th>Age</th>
  </tr>
  <tr>
    <td>Alice</td><td>25</td>
  </tr>
</table>
```

---

## 📝 Lists

* **Ordered List**: `<ol>`
* **Unordered List**: `<ul>`
* **List Item**: `<li>`

```html
<ul>
  <li>Item One</li>
  <li>Item Two</li>
</ul>
```

---

## 🧱 HTML Block vs Inline Elements

* **Block elements**: Start on a new line and take full width
  Examples: `<div>`, `<p>`, `<h1>`–`<h6>`, `<table>`
* **Inline elements**: Do not start on a new line
  Examples: `<span>`, `<a>`, `<img>`, `<strong>`

---

## 🧩 Divs

The `<div>` element is a **generic container** for grouping block-level content.

```html
<div class="section">
  <p>This is inside a div.</p>
</div>
```

Used for layout and styling.

---

## 🎨 Span

The `<span>` tag is a **generic inline container** for grouping inline content.

```html
<p>This is a <span style="color:red;">highlighted</span> word.</p>
```

Used primarily for styling small parts of text.

---

## 🔁 HTML vs XHTML

| Feature          | HTML                      | XHTML                              |
| ---------------- | ------------------------- | ---------------------------------- |
| Syntax           | Flexible                  | Strict                             |
| Closing Tags     | Optional for some         | Required for all                   |
| Case Sensitivity | Not case-sensitive        | Case-sensitive (`<Img>` ≠ `<img>`) |
| Parsing          | Forgiving                 | Strict, XML-based                  |
| DOCTYPE          | `<!DOCTYPE html>` (HTML5) | Must declare XML DTD               |

XHTML is a stricter XML-compliant version of HTML.

---
# HTML5 semantic elements: `header`, `nav`, `section`, `article`, `aside`, and `footer`.

---

## 🔸 `<nav>`

The `<nav>` element defines a section containing **navigation links**.

```html
<nav>
  <ul>
    <li><a href="/home">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

* Helps **screen readers and bots** identify navigation menus.
* Usually contains the main or secondary navigation.

---

## 📦 `<section>`

The `<section>` element defines a **thematic grouping of content**, typically with a heading.

```html
<section>
  <h2>Our Services</h2>
  <p>We offer web development and design.</p>
</section>
```

* Use when content has a **logical grouping** and needs a heading.
* Don’t use `<section>` for generic containers — prefer `<div>` in those cases.

---

## 📰 `<article>`

The `<article>` element represents **self-contained content** that could be independently distributed.

```html
<article>
  <h2>Blog Post Title</h2>
  <p>This blog post talks about semantic HTML...</p>
</article>
```

* Examples: blog posts, forum threads, news articles.
* Each `<article>` may have its own `<header>` and `<footer>`.

---

## 🧾 `<aside>`

The `<aside>` element contains content **indirectly related** to the main content.

```html
<aside>
  <h3>Related Articles</h3>
  <ul>
    <li><a href="#">Semantic Tags Explained</a></li>
    <li><a href="#">HTML5 Cheatsheet</a></li>
  </ul>
</aside>
```

* Think of it as a **sidebar** or **callout box**.
* Can be used **inside or outside** the main content.

---

## 🔻 `<footer>`

The `<footer>` element typically contains **footer information** for a section or page.

```html
<footer>
  <p>&copy; 2025 My Website</p>
  <p><a href="/privacy">Privacy Policy</a></p>
</footer>
```

* Common contents: copyrights, contact info.
* Can appear **once per page** or within each section/article.

---

## ✅ Summary Table

| Tag         | Purpose                                 |
| ----------- | --------------------------------------- |
| `<header>`  | Top/intro part of page or section       |
| `<nav>`     | Navigation links                        |
| `<section>` | Thematic grouping of content            |
| `<article>` | Standalone, distributable content       |
| `<aside>`   | Side content, like ads or related links |
| `<footer>`  | Bottom info (copyright, links, etc.)    |

---

These tags enhance the structure and meaning of your HTML, which is especially helpful for accessibility tools and search engines.


```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Semantic HTML Example</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    header, nav, section, article, aside, footer {
      padding: 1em;
      margin: 0;
    }
    nav {
      background-color: #333;
      color: white;
    }
    nav ul {
      list-style: none;
      display: flex;
      padding: 0;
    }
    nav ul li {
      margin-right: 20px;
    }
    nav ul li a {
      color: white;
      text-decoration: none;
    }
    main {
      display: flex;
    }
    section {
      flex: 3;
      padding: 1em;
    }
    aside {
      flex: 1;
      background: #f0f0f0;
      padding: 1em;
    }
    footer {
      background: #222;
      color: white;
      text-align: center;
    }
  </style>
</head>
<body>

  <header>
    <h1>My Website</h1>
    <p>Learning Semantic HTML Layout</p>
  </header>

  <nav>
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">Blog</a></li>
      <li><a href="#">About</a></li>
    </ul>
  </nav>

  <main>
    <section>
      <article>
        <h2>What is Semantic HTML?</h2>
        <p>Semantic HTML uses HTML5 elements that clearly describe their meaning in a human- and machine-readable way.</p>
      </article>

      <article>
        <h2>Benefits of Semantic Tags</h2>
        <p>They improve SEO, accessibility, and code readability.</p>
      </article>
    </section>

    <aside>
      <h3>Related Topics</h3>
      <ul>
        <li><a href="#">HTML5 New Features</a></li>
        <li><a href="#">Accessibility Basics</a></li>
      </ul>
    </aside>
  </main>

  <footer>
    <p>&copy; 2025 My Website | <a href="#" style="color:white;">Privacy Policy</a></p>
  </footer>

</body>
</html>

```


