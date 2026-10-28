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
.card{background:#1e293b;padding:18px;border-radius:14px;margin:16px 0}
h1{color:#60a5fa}
select{padding:14px;width:100%;border-radius:8px;font-size:17px}
.value{color:#60a5fa;font-size:28px;font-weight:bold}
.note{color:#fbbf24;line-height:1.5}
#chart{width:100%;height:350px}
</style>
</head>
<body>

<h1>Currency Learning 📊</h1>
<p>Educational demo dashboard</p>

<div class="card">
<h3>Select Currency Pair</h3>
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
<div id="chart"></div>
<p class="note">Sample data only — not live market prices.</p>
</div>

<div class="card">
<h3>EMA (5-point)</h3>
<p>Last EMA value:</p>
<div class="value" id="ema">--</div>
<p>EMA helps explain average price movement over time.</p>
</div>

<div class="card">
<h3>RSI (5-point)</h3>
<p>Demo RSI value:</p>
<div class="value" id="rsi">--</div>
<p>RSI is an educational measure of price momentum.</p>
</div>

<div class="card">
<h3>Learning Note</h3>
<p id="lesson">Values are calculated from sample data.</p>
<p class="note">These educational values are not trading advice or predictions.</p>
</div>

<script>
const demoData = {
"EUR/USD":[1.100,1.102,1.101,1.104,1.106,1.103,1.107,1.109,1.106,1.110,1.112,1.108,1.111,1.114,1.113,1.116,1.114,1.118,1.117,1.120],
"GBP/USD":[1.270,1.272,1.269,1.274,1.276,1.273,1.278,1.275,1.280,1.282,1.279,1.284,1.281,1.286,1.288,1.285,1.290,1.287,1.292,1.294],
"USD/JPY":[150.0,150.2,150.1,150.4,150.3,150.6,150.5,150.8,150.7,150.9,150.6,150.8,151.0,150.9,151.2,151.1,151.3,151.2,151.5,151.4],
"AUD/USD":[0.650,0.652,0.651,0.653,0.655,0.652,0.654,0.656,0.655,0.657,0.656,0.659,0.658,0.660,0.659,0.662,0.661,0.663,0.662,0.665],
"USD/CAD":[1.350,1.352,1.351,1.349,1.353,1.354,1.352,1.355,1.357,1.354,1.356,1.358,1.357,1.359,1.361,1.360,1.362,1.361,1.364,1.365]
};

function calculateEMA(data, period){
    const k = 2 / (period + 1);
    let ema = data[0];
    const result = [ema];
    for(let i=1;i<data.length;i++){
        ema = data[i]*k + ema*(1-k);
        result.push(ema);
    }
    return result;
}

function calculateRSI(data, period){
    const result = Array(data.length).fill(null);
    if(data.length <= period) return result;

    for(let i=period;i<data.length;i++){
        let gains=0, losses=0;
        for(let j=i-period+1;j<=i;j++){
            const change=data[j]-data[j-1];
            if(change>0) gains+=change;
            if(change<0) losses-=change;
        }
        if(losses===0){
            result[i]=gains===0 ? 50 : 100;
        } else {
            const rs=(gains/period)/(losses/period);
            result[i]=100-(100/(1+rs));
        }
    }
    return result;
}

function updateDashboard(){
    const pair=document.getElementById("pair").value;
    const prices=demoData[pair];
    const times=prices.map((_,i)=>"Point "+(i+1));
    const ema=calculateEMA(prices,5);
    const rsi=calculateRSI(prices,5);

    document.getElementById("ema").textContent=
        ema[ema.length-1].toFixed(5);

    document.getElementById("rsi").textContent=
        rsi[rsi.length-1].toFixed(2);

    document.getElementById("lesson").textContent=
        pair+" uses its own illustrative sample prices. These values explain EMA and RSI calculations only.";

    Plotly.newPlot("chart",[
        {
            x:times,y:prices,
            type:"scatter",mode:"lines+markers",
            name:"Demo Price",
            line:{color:"#60a5fa"}
        },
        {
            x:times,y:ema,
            type:"scatter",mode:"lines",
            name:"EMA (5)",
            line:{color:"#fbbf24",width:3}
        }
    ],{
        paper_bgcolor:"#1e293b",
        plot_bgcolor:"#1e293b",
        font:{color:"white"},
        margin:{t:20,l:55,r:15,b:70},
        xaxis:{title:"Sample points",tickangle:-45},
        yaxis:{title:"Illustrative price"},
        legend:{orientation:"h"}
    },{responsive:true});
}

document.getElementById("pair").addEventListener("change",updateDashboard);
updateDashboard();
</script>
</body>
</html>
"""

@app.get("/health")
def health():
    return {"status":"healthy"}
