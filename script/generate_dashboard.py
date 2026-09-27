import json
import os
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

USER = "CodeMaster11000"
TOKEN = os.environ.get("GITHUB_TOKEN")

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}",
    headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
    },
)

with urllib.request.urlopen(req, timeout=20) as response:
    user = json.load(response)

repos = user.get("public_repos", 0)
followers = user.get("followers", 0)
updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")

svg = f'''<svg width="1200" height="390" viewBox="0 0 1200 390" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1200" y2="390"><stop stop-color="#0D1117"/><stop offset=".55" stop-color="#111827"/><stop offset="1" stop-color="#0B1220"/></linearGradient>
  <linearGradient id="accent" x1="100" y1="0" x2="1000" y2="390"><stop stop-color="#58A6FF"/><stop offset=".5" stop-color="#8957E5"/><stop offset="1" stop-color="#2EA043"/></linearGradient>
  <filter id="glow"><feGaussianBlur stdDeviation="7" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" stroke="#30363D" stroke-opacity=".25"/></pattern>
</defs>
<rect width="1200" height="390" rx="18" fill="url(#bg)"/>
<rect width="1200" height="390" rx="18" fill="url(#grid)"/>
<circle cx="1050" cy="90" r="155" fill="#238636" opacity=".07" filter="url(#glow)"/>
<circle cx="930" cy="280" r="170" fill="#58A6FF" opacity=".06" filter="url(#glow)"/>
<rect x="42" y="34" width="1116" height="1" fill="#30363D"/>
<circle cx="60" cy="20" r="5" fill="#FF7B72"/><circle cx="78" cy="20" r="5" fill="#D29922"/><circle cx="96" cy="20" r="5" fill="#3FB950"/>
<text x="52" y="88" fill="#8B949E" font-family="monospace" font-size="14">EKANSH / SOFTWARE DEVELOPER</text>
<text x="52" y="142" fill="#F0F6FC" font-family="system-ui, sans-serif" font-size="48" font-weight="700">Hi, I'm Ekansh.</text>
<text x="52" y="178" fill="#58A6FF" font-family="monospace" font-size="18">BUILDING • LEARNING • SHIPPING</text>
<text x="52" y="220" fill="#8B949E" font-family="system-ui, sans-serif" font-size="16">B.Tech Computer Science @ SKIT Jaipur</text>
<text x="52" y="247" fill="#8B949E" font-family="system-ui, sans-serif" font-size="16">Full-stack Java + Angular  ·  AI/ML  ·  DevOps</text>
<rect x="52" y="278" width="530" height="58" rx="10" fill="#161B22" stroke="#30363D"/>
<circle cx="77" cy="307" r="7" fill="#3FB950"/>
<text x="96" y="302" fill="#8B949E" font-family="monospace" font-size="12">CURRENTLY BUILDING</text>
<text x="96" y="322" fill="#F0F6FC" font-family="monospace" font-size="15" font-weight="700">SkyGuard AI</text>
<rect x="642" y="62" width="475" height="270" rx="16" fill="#0D1117" stroke="url(#accent)" stroke-width="1.5"/>
<text x="674" y="96" fill="#58A6FF" font-family="monospace" font-size="13">FEATURED PROJECT</text>
<text x="674" y="140" fill="#F0F6FC" font-family="system-ui, sans-serif" font-size="31" font-weight="700">☁ SkyGuard AI</text>
<text x="674" y="171" fill="#8B949E" font-family="system-ui, sans-serif" font-size="14">AI anomaly detection for</text>
<text x="674" y="192" fill="#8B949E" font-family="system-ui, sans-serif" font-size="14">Automatic Weather Stations</text>
<g font-family="monospace" font-size="11">
<rect x="674" y="215" width="78" height="25" rx="12" fill="#1F6FEB" fill-opacity=".18" stroke="#1F6FEB" stroke-opacity=".45"/><text x="690" y="231" fill="#58A6FF">PYTHON</text>
<rect x="760" y="215" width="72" height="25" rx="12" fill="#8957E5" fill-opacity=".18" stroke="#8957E5" stroke-opacity=".45"/><text x="779" y="231" fill="#C8A6FF">ML</text>
<rect x="840" y="215" width="80" height="25" rx="12" fill="#238636" fill-opacity=".18" stroke="#238636" stroke-opacity=".45"/><text x="858" y="231" fill="#3FB950">JAVA</text>
<rect x="928" y="215" width="91" height="25" rx="12" fill="#1F6FEB" fill-opacity=".18" stroke="#1F6FEB" stroke-opacity=".45"/><text x="942" y="231" fill="#58A6FF">SPRING</text>
<rect x="674" y="251" width="110" height="25" rx="12" fill="#238636" fill-opacity=".18" stroke="#238636" stroke-opacity=".45"/><text x="694" y="267" fill="#3FB950">TIMESCALE</text>
<rect x="792" y="251" width="75" height="25" rx="12" fill="#8957E5" fill-opacity=".18" stroke="#8957E5" stroke-opacity=".45"/><text x="812" y="267" fill="#C8A6FF">KAFKA</text>
<rect x="875" y="251" width="80" height="25" rx="12" fill="#1F6FEB" fill-opacity=".18" stroke="#1F6FEB" stroke-opacity=".45"/><text x="894" y="267" fill="#58A6FF">DOCKER</text>
<text x="674" y="307" fill="#8B949E">SIH 2026</text><text x="755" y="307" fill="#3FB950">●</text><text x="772" y="307" fill="#F0F6FC">SIH26073</text>
<text x="990" y="307" fill="#8B949E" font-size="10">LIVE PROFILE</text>
<text x="990" y="324" fill="#58A6FF" font-size="10">{repos} repos · {followers} followers</text>
</g>
<text x="52" y="365" fill="#484F58" font-family="monospace" font-size="9">AUTO-UPDATED {updated} · github.com/{USER}</text>
</svg>'''

Path("assets/ekansh-dashboard.svg").write_text(svg, encoding="utf-8")
