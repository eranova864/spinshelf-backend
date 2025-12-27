from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def form():
    return """
    <form method="post" action="/calculate">
      Diameter: <input name="diameter" type="number" required><br>
      Height: <input name="height" type="number" required><br>
      Levels: <input name="levels" type="number" required><br>
      <button type="submit">Calculate price</button>
    </form>
    """

@app.post("/calculate", response_class=HTMLResponse)
def calculate(
    diameter: int = Form(...),
    height: int = Form(...),
    levels: int = Form(...)
):
    price = diameter * height * levels * 0.1
    return f"<h2>Price: {price:.2f}</h2><a href='/'>Back</a>"
