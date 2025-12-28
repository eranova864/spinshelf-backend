from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def form():
    return """
    <html>
    <head>
      <style>
        body {
          font-family: Arial, sans-serif;
          background: #f7f7f7;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          margin: 0;
        }
        .card {
          background: white;
          padding: 24px;
          border-radius: 8px;
          width: 320px;
        }
        input, button {
          width: 100%;
          padding: 8px;
          margin-top: 8px;
        }
        button {
          background: #000;
          color: white;
          border: none;
          cursor: pointer;
        }
      </style>
    </head>
    <body>
      <div class="card">
        <form method="post" action="/calculate">
          <input name="diameter" type="number" placeholder="Діаметр" required>
          <input name="height" type="number" placeholder="Висота" required>
          <input name="levels" type="number" placeholder="Кількість ярусів" required>
          <button type="submit">Розрахувати ціну</button>
        </form>
      </div>
    </body>
    </html>
    """


@app.post("/calculate", response_class=HTMLResponse)
def calculate(
    diameter: int = Form(...),
    height: int = Form(...),
    levels: int = Form(...)
):
    price = diameter**2 * levels * 2
    return f"<h2>Price: {price:.2f}</h2><a href='/'>Back</a>"
