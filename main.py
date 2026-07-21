from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
import random

app = FastAPI( 
    title="Fun API",
    description="A simple and fun API.",
    version="1.0.0",
    )

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fun API</title>
    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, Helvetica, sans-serif;
        }

        body{
            background:linear-gradient(135deg,#4F46E5,#06B6D4);
            min-height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            color:white;
        }

        .card{
            width:90%;
            max-width:700px;
            background:rgba(255,255,255,0.12);
            backdrop-filter:blur(15px);
            border:1px solid rgba(255,255,255,0.2);
            border-radius:20px;
            padding:40px;
            box-shadow:0 20px 40px rgba(0,0,0,.25);
        }

        h1{
            font-size:3rem;
            margin-bottom:10px;
        }

        p{
            opacity:.9;
            margin-bottom:30px;
            line-height:1.6;
        }

        h2{
            margin-bottom:15px;
        }

        .endpoint{
            background:rgba(255,255,255,.15);
            padding:15px 20px;
            border-radius:12px;
            margin:10px 0;
            display:flex;
            justify-content:space-between;
            transition:.25s;
        }

        .endpoint:hover{
            transform:translateX(6px);
            background:rgba(255,255,255,.22);
        }

        code{
            color:#FDE68A;
            font-size:1rem;
        }

        footer{
            margin-top:30px;
            text-align:center;
            opacity:.75;
            font-size:.9rem;
        }
    </style>
</head>

<body>

<div class="card">
    <h1>🎲 Fun API</h1>

    <p>
        Welcome to <strong>Fun API</strong>, a small FastAPI project created by
        <strong>Jishnu Dutta</strong> for learning Docker, FastAPI, and backend
        development.
    </p>

    <h2>Available Endpoints</h2>

    <div class="endpoint">
        <code>GET /roll</code>
        <span>🎲 Roll one die</span>
    </div>

    <div class="endpoint">
        <code>GET /roll/{count}</code>
        <span>🎲 Roll multiple dice</span>
    </div>

     <div class="endpoint">
        <code>GET /flip</code>
        <span>🪙 Flip a coin</span>
    </div>

    <div class="endpoint">
        <code>GET /flip/{count}</code>
        <span>🪙 Flip a coin multiple times</span>
    </div>
    
    <div class="endpoint">
        <code>GET /gradient</code>
        <span>🎨 Beautiful random gradient page</span>
    </div>

    <div class="endpoint">
        <code>GET /gradient/json</code>
        <span>📦 Gradient data in JSON format</span>
    </div>

    <div class="endpoint">
        <code>GET /docs</code>
        <span>📖 Interactive API Docs</span>
    </div>

    <footer>
        Built with ❤️ using FastAPI
    </footer>
</div>

</body>
</html>
"""


@app.get("/roll")
async def roll():
    roll = random.randint(1,6)
   
    return{"roll": roll}

@app.get("/roll/{count}")
async def roll_multiple(count: int):
    if count < 1 or count > 200:
        raise HTTPException(
            status_code=400,
            detail="Count must be between 1 and 200."
        )

    rolls = [random.randint(1, 6) for _ in range(count)]

    return {
        "count": count,
        "rolls": rolls,
        "total": sum(rolls)
    }

@app.get("/flip")
async def flip():
    coin = random.choice(["Heads", "Tails"])
   
    return{"coin":coin}

@app.get("/flip/{count}")
async def flip(count:int):
    if count < 1 or count > 200:
        raise HTTPException(
            status_code=400,
            detail="Count must be between 1 and 200."
        )
    heads = 0
    tails = 0
    flips = []

    for _ in range(count):
        face = random.choice(["Heads", "Tails"])
        flips.append(face)
        if face == "Heads" :
            heads += 1
        else:
            tails += 1
   
    return{
        "count":count,
        "heads": heads,
        "tails": tails,
        "flips":flips
    }
GRADIENTS = [
    {"name": "Royal Purple", "colors": ["#667eea", "#764ba2"]},
    {"name": "Pink Sunset", "colors": ["#f093fb", "#f5576c"]},
    {"name": "Blue Sky", "colors": ["#4facfe", "#00f2fe"]},
    {"name": "Mint Breeze", "colors": ["#43e97b", "#38f9d7"]},
    {"name": "Golden Sunrise", "colors": ["#fa709a", "#fee140"]},
    {"name": "Deep Ocean", "colors": ["#30cfd0", "#330867"]},
    {"name": "Lavender Dream", "colors": ["#a18cd1", "#fbc2eb"]},
    {"name": "Peach Glow", "colors": ["#f6d365", "#fda085"]},
    {"name": "Spring Meadow", "colors": ["#84fab0", "#8fd3f4"]},
    {"name": "Candy Pop", "colors": ["#fccb90", "#d57eeb"]},
    {"name": "Rose Bloom", "colors": ["#ff9a9e", "#fecfef"]},
    {"name": "Frozen Lake", "colors": ["#a1c4fd", "#c2e9fb"]},
    {"name": "Fresh Lime", "colors": ["#d4fc79", "#96e6a1"]},
    {"name": "Blue Horizon", "colors": ["#667db6", "#0082c8"]},
    {"name": "Sea Foam", "colors": ["#00cdac", "#8ddad5"]},
    {"name": "Summer Heat", "colors": ["#ff9966", "#ff5e62"]},
    {"name": "Neon Violet", "colors": ["#7F00FF", "#E100FF"]},
    {"name": "Crystal Water", "colors": ["#00B4DB", "#0083B0"]},
    {"name": "Azure Flow", "colors": ["#56CCF2", "#2F80ED"]},
    {"name": "Electric Blue", "colors": ["#6a11cb", "#2575fc"]},
    {"name": "Cherry Flame", "colors": ["#ee0979", "#ff6a00"]},
    {"name": "Lagoon", "colors": ["#2193b0", "#6dd5ed"]},
    {"name": "Berry Wine", "colors": ["#cc2b5e", "#753a88"]},
    {"name": "Twilight", "colors": ["#42275a", "#734b6d"]},
    {"name": "Steel Night", "colors": ["#bdc3c7", "#2c3e50"]},
    {"name": "Soft Coral", "colors": ["#de6262", "#ffb88c"]},
    {"name": "Turquoise Bay", "colors": ["#06beb6", "#48b1bf"]},
    {"name": "Fire Ember", "colors": ["#eb3349", "#f45c43"]},
    {"name": "Blush Pink", "colors": ["#dd5e89", "#f7bb97"]},
    {"name": "Mystic River", "colors": ["#614385", "#516395"]},
    {"name": "Tropical Aqua", "colors": ["#02aab0", "#00cdac"]},
    {"name": "Orange Burst", "colors": ["#fc4a1a", "#f7b733"]},
    {"name": "Forest Stream", "colors": ["#5f2c82", "#49a09d"]},
    {"name": "Cool Breeze", "colors": ["#24c6dc", "#514a9d"]},
    {"name": "Ruby Glow", "colors": ["#ff512f", "#dd2476"]},
    {"name": "Royal Orchid", "colors": ["#4568dc", "#b06ab3"]},
    {"name": "Dark Velvet", "colors": ["#c31432", "#240b36"]},
    {"name": "Golden Flame", "colors": ["#f12711", "#f5af19"]},
    {"name": "Emerald Valley", "colors": ["#1d976c", "#93f9b9"]},
    {"name": "Scarlet Rush", "colors": ["#ff416c", "#ff4b2b"]},
    {"name": "Midnight Navy", "colors": ["#141e30", "#243b55"]},
    {"name": "Purple Haze", "colors": ["#3a1c71", "#d76d77"]},
    {"name": "Blue Aurora", "colors": ["#4e54c8", "#8f94fb"]},
    {"name": "Soft Lilac", "colors": ["#654ea3", "#eaafc8"]},
    {"name": "Cotton Candy", "colors": ["#ff758c", "#ff7eb3"]},
    {"name": "Galaxy Mist", "colors": ["#3f2b96", "#a8c0ff"]},
    {"name": "Crimson Sky", "colors": ["#c33764", "#1d2671"]},
    {"name": "Bubblegum", "colors": ["#fc5c7d", "#6a82fb"]},
    {"name": "Ocean Wave", "colors": ["#00d2ff", "#3a7bd5"]},
    {"name": "Sunflower", "colors": ["#f7971e", "#ffd200"]},
    {"name": "Wine Red", "colors": ["#7b4397", "#dc2430"]},
    {"name": "Mint Splash", "colors": ["#00c9ff", "#92fe9d"]},
    {"name": "Soft Blush", "colors": ["#ffdde1", "#ee9ca7"]},
    {"name": "Warm Sand", "colors": ["#ffecd2", "#fcb69f"]},
    {"name": "Pink Velvet", "colors": ["#f953c6", "#b91d73"]},
    {"name": "Sea Depth", "colors": ["#43cea2", "#185a9d"]},
    {"name": "Coral Shine", "colors": ["#ff0844", "#ffb199"]},
    {"name": "Dream Violet", "colors": ["#a770ef", "#cf8bf3"]},
    {"name": "Cyber Mint", "colors": ["#2af598", "#009efd"]},
    {"name": "Honey Gold", "colors": ["#ffb347", "#ffcc33"]},
    {"name": "Ice Crystal", "colors": ["#7de2fc", "#b9b6e5"]},
    {"name": "Cherry Blossom", "colors": ["#ff6a88", "#ff99ac"]},
    {"name": "Morning Dew", "colors": ["#5ee7df", "#b490ca"]},
    {"name": "Polar Sky", "colors": ["#89f7fe", "#66a6ff"]},
    {"name": "Dreamy Pink", "colors": ["#9796f0", "#fbc7d4"]},
    {"name": "Coral Dawn", "colors": ["#ff8177", "#ff867a"]},
    {"name": "Glacier", "colors": ["#74ebd5", "#acb6e5"]},
    {"name": "Soft Orchid", "colors": ["#d299c2", "#fef9d7"]},
    {"name": "Blue Whisper", "colors": ["#accbee", "#e7f0fd"]},
    {"name": "Silver Cloud", "colors": ["#cfd9df", "#e2ebf0"]},
    {"name": "Vanilla Cream", "colors": ["#fdfcfb", "#e2d1c3"]},
    {"name": "Lilac Sky", "colors": ["#d9afd9", "#97d9e1"]},
    {"name": "Neon Pop", "colors": ["#89fffd", "#ef32d9"]},
    {"name": "Green Energy", "colors": ["#00f260", "#0575e6"]},
    {"name": "Tangerine", "colors": ["#ff8a00", "#e52e71"]},
    {"name": "Royal Blue", "colors": ["#4776e6", "#8e54e9"]},
    {"name": "Dark Rose", "colors": ["#3c1053", "#ad5389"]},
    {"name": "Green Paradise", "colors": ["#11998e", "#38ef7d"]},
    {"name": "Berry Blue", "colors": ["#fc466b", "#3f5efb"]},
    {"name": "Cotton Violet", "colors": ["#12c2e9", "#c471ed"]},
    {"name": "Sunset Bloom", "colors": ["#f64f59", "#c471ed"]},
    {"name": "Arctic Blue", "colors": ["#1fa2ff", "#12d8fa"]},
    {"name": "Jungle Mist", "colors": ["#8360c3", "#2ebf91"]},
    {"name": "Pastel Peach", "colors": ["#ffafbd", "#ffc3a0"]},
    {"name": "Spring Garden", "colors": ["#c6ffdd", "#fbd786"]},
    {"name": "Emerald Glow", "colors": ["#84fab0", "#16a085"]},
    {"name": "Golden Honey", "colors": ["#ffe259", "#ffa751"]},
    {"name": "Cherry Cream", "colors": ["#ed4264", "#ffedbc"]},
    {"name": "Forest Morning", "colors": ["#1f4037", "#99f2c8"]},
    {"name": "Magenta Noir", "colors": ["#ff0099", "#493240"]},
    {"name": "Fresh Citrus", "colors": ["#30e8bf", "#ff8235"]},
    {"name": "Blue Lagoon", "colors": ["#6dd5fa", "#2980b9"]},
    {"name": "Autumn Plum", "colors": ["#e96443", "#904e95"]},
    {"name": "Cosmic Purple", "colors": ["#8e2de2", "#4a00e0"]},
    {"name": "Sunrise Gold", "colors": ["#ff4e50", "#f9d423"]},
    {"name": "Pink Passion", "colors": ["#f857a6", "#ff5858"]},
    {"name": "Mint Ice", "colors": ["#0cebeb", "#20e3b2"]},
    {"name": "Peach Sunset", "colors": ["#ff7e5f", "#feb47b"]},
    {"name": "Blue Mist", "colors": ["#36d1dc", "#5b86e5"]},
    {"name": "Purple Tide", "colors": ["#5b247a", "#1bcedf"]},
    {"name": "Graphite", "colors": ["#232526", "#414345"]},
    {"name": "Dusky Evening", "colors": ["#355c7d", "#6c5b7b"]}
]

@app.get("/gradient/json")
async def gradient():
    gradientColor = random.choice(GRADIENTS)
    angle = random.randint(1,360)
    color1 = gradientColor['colors'][0]
    color2 = gradientColor['colors'][1]
    name = gradientColor['name']
    return{
    "name": name,
    "angle": angle,
    "colors": [
        color1,
        color2
    ],
    "css": f"linear-gradient({angle}deg, {color1}, {color2})"
}

@app.get("/gradient", response_class=HTMLResponse)
async def gradient():
    gradientColor = random.choice(GRADIENTS)
    angle = random.randint(1,360)
    color1 = gradientColor['colors'][0]
    color2 = gradientColor['colors'][1]
    name = gradientColor['name']
    css = f"linear-gradient({angle}deg, {color1}, {color2})"
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name}</title>

<style>
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Inter, Arial, sans-serif;
    background: {css};
    color: white;
}}

.card {{
    width: min(600px, 90%);
    backdrop-filter: blur(18px);
    background: rgba(255,255,255,.15);
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 24px;
    padding: 32px;
    box-shadow: 0 20px 50px rgba(0,0,0,.25);
}}

h1 {{
    font-size: 2.2rem;
    margin-bottom: 8px;
}}

.subtitle {{
    opacity: .8;
    margin-bottom: 24px;
}}

.code {{
    background: rgba(0,0,0,.25);
    padding: 16px;
    border-radius: 12px;
    font-family: monospace;
    word-break: break-word;
}}

.colors {{
    display: flex;
    gap: 16px;
    margin: 28px 0;
}}

.color {{
    flex: 1;
    text-align: center;
}}

.swatch {{
    height: 70px;
    border-radius: 12px;
    border: 2px solid rgba(255,255,255,.3);
    margin-bottom: 10px;
}}

.buttons {{
    display: flex;
    gap: 12px;
    margin-top: 24px;
}}

button {{
    flex: 1;
    padding: 14px;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    font-size: 16px;
    font-weight: 600;
    transition: .25s;
}}

button:hover {{
    transform: translateY(-2px);
}}

.copy {{
    background: white;
    color: black;
}}

.new {{
    background: rgba(255,255,255,.2);
    color: white;
}}

footer {{
    margin-top: 20px;
    text-align: center;
    opacity: .7;
    font-size: .9rem;
}}
</style>

</head>
<body>

<div class="card">

<h1>🎨 {name}</h1>

<p class="subtitle">
Beautiful Random Gradient
</p>

<div class="code" id="css">
{css}
</div>

<div class="colors">

<div class="color">
<div class="swatch" style="background:{color1}"></div>
<b>{color1}</b>
</div>

<div class="color">
<div class="swatch" style="background:{color2}"></div>
<b>{color2}</b>
</div>

</div>

<div class="buttons">
<button class="copy" onclick="copyCSS()">
📋 Copy CSS
</button>

<button class="new" onclick="location.reload()">
🎲 New Gradient
</button>
</div>

<footer>
Generated by Fun API ✨
</footer>

</div>

<script>
function copyCSS() {{
    navigator.clipboard.writeText(document.getElementById("css").innerText);

    const btn = document.querySelector(".copy");

    btn.innerText = "✅ Copied!";

    setTimeout(() => {{
        btn.innerText = "📋 Copy CSS";
    }},1500);
}}
</script>

</body>
</html>
"""