from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Currency Learning Dashboard")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Currency Learning Dashboard</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background: #101827;
          color: white;
          padding: 20px;
        }
        .card {
          background: #1e293b;
          padding: 18px;
          border-radius: 14px;
          margin: 15px 0;
        }
        h1 { color: #60a5fa; }
        select {
          padding: 12px;
          width: 100%;
          border-radius: 8px;
        }
        .note { color: #fbbf24; }
      </style>
    </head>
    <body>
      <h1>Currency Learning 📊</h1>
      <p>Welcome to your learning dashboard!</p>

      <div class="card">
        <h3>Select Currency Pair</h3>
        <select id="pair">
          <option>EUR/USD</option>
          <option>GBP/USD</option>
          <option>USD/JPY</option>
          <option>AUD/USD</option>
          <option>USD/CAD</option>
        </select>
        <p id="selected">Selected: EUR/USD</p>
      </div>

      <div class="card">
        <h3>EMA — Learning</h3>
        <p>EMA helps explain average price movement over time.</p>
      </div>

      <div class="card">
        <h3>RSI — Learning</h3>
        <p>RSI is an indicator used to study price momentum.</p>
      </div>

      <div class="card">
        <h3>Practice Mode</h3>
        <p class="note">Demo learning only — no real trading signals.</p>
        <p>Use historical or sample data to learn indicators.</p>
      </div>

      <script>
        document.getElementById("pair").onchange = function() {
          document.getElementById("selected").textContent =
            "Selected: " + this.value;
        };
      </script>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "healthy"}
