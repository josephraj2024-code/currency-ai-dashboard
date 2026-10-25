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
.value{font-size:24px;color:#60a5fa;font-weight:bold}
.note{color:#fbbf24}
</style>
</head>
<body>
<h1>Currency Learning 📊</h1>
<p>Educational demo dashboard</p>

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
<div id="chart" style="width:100%;height:300px"></div>
<p class="note">Sample data only — not live market prices.</p>
</div>

<div class="card">
<h3>EMA (5-point)</h3>
<p>Last EMA value:</p>
<div class="value" id="ema">Calculating...</div>
<p>EMA என்பது விலைகளின் சராசரி நகர்வைக் கற்க உதவும்.</p>
</div>

<div class="card">
<h3>RSI (5-point)</h3>
<p>Demo RSI value:</p>
<div class="value" id="rsi">Calculating...</div>
<p>RSI என்பது விலை நகர்வின் வேகத்தைப் புரிந்துகொள்ள உதவும்.</p>
</div>

<div class="card">
<h3>Learning Note</h3>
<p id="lesson">கணக்கீடுகள் தயாராகின்றன.</p>
<p class="note">இந்த எண்கள் கல்விக்கானவை மட்டுமே. வாங்க/விற்கும் சிக்னல்கள் அல்ல.</p>
</div>

<script>
const prices = [
1.100,1.102,1.101,1.104,1.106,
1.103,1.107,1.109,1.106,1.110,
1.112,1.108,1.111,1.114,1.113,
1.116,1.114,1.118,1.117,1.120
];

function calculateEMA(data, period){
  const k = 2 / (period + 1);
  let ema = data[0];
  const values = [ema];
  for(let i=1; i<data.length; i++){
    ema = data[i] * k + ema * (1-k);
    values.push(ema);
  }
  return values;
}

function calculateRSI(data, period){
  if(data.length <= period) return null;
  let gains = 0, losses = 0;
  for(let i=1; i<=period; i++){
    const change = data[i] - data[i-1];
    if(change > 0) gains += change;
    else losses -= change;
  }
  let avgGain = gains / period;
  let avgLoss = losses / period;

  for(let i=period+1; i<data.length; i++){
    const change = data[i] - data[i-1];
    avgGain = (avgGain*(period-1) + Math.max(change,0))/period;
    avgLoss = (avgLoss*(period-1) + Math.max(-change,0))/period;
  }

  if(avgLoss === 0) return 100;
  const rs = avgGain / avgLoss;
  return 100 - (100/(1+rs));
}

const emaValues = calculateEMA(prices,5);
const rsiValue = calculateRSI(prices,5);

document.getElementById("ema").textContent =
  emaValues[emaValues.length-1].toFixed(5);

document.getElementById("rsi").textContent =
  rsiValue === null ? "Not enough data" : rsiValue.toFixed(2);

document.getElementById("lesson").textContent =
  "EMA மற்றும் RSI கணக்கீடுகள் Demo விலைகளிலிருந்து உருவாக்கப்பட்டுள்ளன. இவை எதிர்கால விலையை உறுதி செய்யாது.";

const times = prices.map((_,i)=>"Point "+(i+1));
const pair = document.getElementById("pair");

function drawChart(){
  Plotly.newPlot("chart",[{
    x:times,
    y:prices,
    type:"scatter",
    mode:"lines+markers",
    line:{color:"#60a5fa"}
  }],{
    paper_bgcolor:"#1e293b",
    plot_bgcolor:"#1e293b",
    font:{color:"white"},
    margin:{t:15,l:50,r:10,b:45},
    xaxis:{title:"Sample points"},
    yaxis:{title:"Illustrative price"}
  },{responsive:true});
}

drawChart();

pair.onchange=function(){
  document.querySelector("body > p").textContent =
    "Selected pair: "+pair.value+" — Demo data only";
};

</script>
</body>
</html>
"""

@app.get("/health")
def health():
    return {"status":"healthy"}
