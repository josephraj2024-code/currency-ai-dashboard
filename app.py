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
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
body{font-family:Arial;background:#101827;color:white;padding:16px}
.card{background:#1e293b;padding:16px;border-radius:14px;margin:16px 0}
h1{color:#60a5fa}
select{padding:12px;width:100%;border-radius:8px}
.note{color:#fbbf24}
</style>
</head>
<body>
<h1>Currency Learning 📊</h1>
<p>Demo chart for learning only</p>

<div class="card">
<h3>Currency Pair</h3>
<select id="pair">
<option>EUR/USD</option>
<option>GBP/USD</option>
<option>USD/JPY</option>
<option>AUD/USD</option>
<option>USD/CAD</option>
</select>
</div>

<div class="card">
<h3>Demo Price Chart</h3>
<div id="chart" style="width:100%;height:350px"></div>
<p class="note">Sample data only — not live market prices or trading signals.</p>
</div>

<div class="card">
<h3>EMA — Learning</h3>
<p>EMA explains average price movement over time.</p>
</div>

<div class="card">
<h3>RSI — Learning</h3>
<p>RSI is used to study price momentum.</p>
</div>

<script>
const prices=[1.101,1.104,1.102,1.107,1.105,1.109,1.106,1.111,1.108,1.113,1.110,1.115];
const times=prices.map((_,i)=>"Point "+(i+1));
function drawChart(){
Plotly.newPlot("chart",[{
x:times,y:prices,type:"scatter",mode:"lines+markers",
line:{color:"#60a5fa"}
}],{
paper_bgcolor:"#1e293b",plot_bgcolor:"#1e293b",
font:{color:"white"},
margin:{t:15,l:45,r:10,b:45},
xaxis:{title:"Sample points"},
yaxis:{title:"Illustrative price"}
},{responsive:true});
}
drawChart();
document.getElementById("pair").onchange=function(){
document.querySelector("body > p").textContent=
"Demo chart selected: "+this.value;
};
</script>
</body>
</html>
"""

@app.get("/health")
def health():
    return {"status":"healthy"}
