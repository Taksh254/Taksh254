"""Builds dark.svg and light.svg (the profile card). Edit ROWS, then run: python3 hero.py"""
from html import escape as e
TH = {
 'dark':  dict(bg='#070B16', panel='#0A101F', bar='#0B1222', line='rgba(255,255,255,0.10)', muted='#475569', label='#22D3EE', text='#F8FAFC', sub='#94A3B8', dot='#334155', a1='#A78BFA', a2='#22D3EE', a3='#10B981', pill='#4C1D95', pilltext='#F8FAFC', chip='#1E1B4B', chipline='#6D28D9', chiptext='#C4B5FD'),
 'light': dict(bg='#F8FAFC', panel='#FFFFFF', bar='#F1F5F9', line='rgba(15,23,42,0.10)', muted='#94A3B8', label='#0891B2', text='#0F172A', sub='#475569', dot='#CBD5E1', a1='#7C3AED', a2='#0891B2', a3='#059669', pill='#7C3AED', pilltext='#FFFFFF', chip='#EDE9FE', chipline='#A78BFA', chiptext='#5B21B6'),
}
ROWS = [
 ('Subject','Taksh Sehrawat'), ('Role','Backend Developer'), ('Status','Building GrowNova OS'),
 ('Focus','APIs, data models, real-time'), ('ToolChain','VS Code, Git, Fedora, Swagger'), None,
 ('Core.Lang','TypeScript, JavaScript'), ('Core.Backend','NestJS, Node.js'),
 ('Core.Database','PostgreSQL, Prisma, Redis'), ('Core.Realtime','Socket.IO, BullMQ'),
 ('Core.AI','LLM APIs, rules engines'), 'Contact',
 ('Grid.GitHub','@Taksh254'), ('Grid.Project','GrowNova OS'),
]
CW = 7.8  # approx width of one 13px monospace char

def hero(t):
    c = TH[t]; o = []
    o.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="560" viewBox="0 0 1180 560" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace" role="img" aria-label="Taksh Sehrawat, backend developer">
<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c['a1']}"><animate attributeName="stop-color" values="{c['a1']};{c['a2']};{c['a3']};{c['a1']}" dur="10s" repeatCount="indefinite"/></stop><stop offset="1" stop-color="{c['a3']}"><animate attributeName="stop-color" values="{c['a3']};{c['a1']};{c['a2']};{c['a3']}" dur="10s" repeatCount="indefinite"/></stop></linearGradient>
<pattern id="dots" width="7" height="7" patternUnits="userSpaceOnUse"><rect width="4" height="4" fill="{c['a1']}"/></pattern>
<mask id="logo"><text x="236" y="350" text-anchor="middle" font-size="190" font-weight="700" fill="#fff">{{ }}</text></mask>
</defs>
<rect x="1" y="1" width="1178" height="558" rx="18" fill="{c['panel']}" stroke="url(#g)" stroke-width="2"/>
<path d="M1 19a18 18 0 0 1 18-18h1142a18 18 0 0 1 18 18v28H1z" fill="{c['bar']}"/>
<line x1="1" y1="47" x2="1179" y2="47" stroke="{c['line']}"/>
<circle cx="30" cy="24" r="5.5" fill="#ff5f56"/><circle cx="50" cy="24" r="5.5" fill="#ffbd2e"/><circle cx="70" cy="24" r="5.5" fill="#27c93f"/>
<text x="590" y="28" text-anchor="middle" font-size="12" fill="{c['sub']}">taksh@fedora - % ./profile.sh --live</text>
<text x="38" y="74" font-size="10" letter-spacing="3" fill="{c['muted']}">VISUAL.MAP</text>
<rect x="36" y="84" width="400" height="440" rx="10" fill="{c['bg']}" stroke="{c['label']}" stroke-opacity="0.4"/>
<g mask="url(#logo)"><rect x="36" y="84" width="400" height="440" fill="url(#dots)" opacity="0"><animate attributeName="opacity" values="0;1" dur="1.2s" begin="0.3s" fill="freeze"/></rect></g>
<text x="236" y="420" text-anchor="middle" font-size="13" letter-spacing="2" fill="{c['sub']}" opacity="0">nest · prisma · redis<animate attributeName="opacity" values="0;1" dur="0.6s" begin="1.4s" fill="freeze"/></text>
<text x="470" y="106" font-size="13" font-weight="700" letter-spacing="2" fill="{c['label']}">SYSTEM.INFO</text>
<line x1="590" y1="102" x2="1060" y2="102" stroke="{c['line']}"/>
<circle cx="1084" cy="102" r="3.5" fill="{c['a3']}"><animate attributeName="opacity" values="1;0.2;1" dur="1.6s" repeatCount="indefinite"/></circle>
<text x="1124" y="106" text-anchor="end" font-size="11" font-weight="700" fill="{c['a3']}">LIVE</text>
<rect x="470" y="122" width="180" height="22" rx="5" fill="{c['pill']}"/>
<text x="560" y="138" text-anchor="middle" font-size="13" font-weight="700" fill="{c['pilltext']}">github.com/Taksh254</text>
''')
    y = 170; i = 0
    for r in ROWS:
        b = 0.5 + i * 0.12; i += 1
        if r is None: y += 10; continue
        if r == 'Contact':
            y += 10
            o.append(f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.3s" begin="{b:.2f}s" fill="freeze"/><text x="470" y="{y}" font-size="13" fill="{c["sub"]}">- Contact</text><line x1="550" y1="{y-4}" x2="1124" y2="{y-4}" stroke="{c["line"]}"/></g>')
            y += 23; continue
        k, v = r
        x1 = 470 + len(k) * CW + 12; x2 = 1124 - len(v) * CW - 12
        o.append(f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.3s" begin="{b:.2f}s" fill="freeze"/><text x="470" y="{y}" font-size="13" fill="{c["label"]}">{e(k)}</text><line x1="{x1:.0f}" y1="{y-4}" x2="{x2:.0f}" y2="{y-4}" stroke="{c["dot"]}" stroke-dasharray="1 5" stroke-linecap="round"/><text x="1124" y="{y}" text-anchor="end" font-size="13" font-weight="700" fill="{c["text"]}">{e(v)}</text></g>')
        y += 23
    b = 0.5 + i * 0.12
    o.append(f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.3s" begin="{b:.2f}s" fill="freeze"/><text x="470" y="{y+8}" font-size="13" fill="{c["sub"]}">▸ Projects and stats below ↓</text><rect x="694" y="{y-5}" width="9" height="16" fill="{c["label"]}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect></g>')
    o.append('</svg>\n')
    return '\n'.join(o)

for t in TH:
    open(f'{t}.svg', 'w').write(hero(t))
