import sys, markdown, datetime
md_path, html_path, title = sys.argv[1], sys.argv[2], sys.argv[3]
with open(md_path, encoding='utf-8') as f:
    text = f.read()
body = markdown.markdown(text, extensions=['tables','fenced_code','toc','attr_list'])
CSS = """
:root{--ink:#1a1d21;--muted:#5b6570;--line:#e3e7ec;--bg:#ffffff;--soft:#f6f8fa;--accent:#2c5f4f;--warn:#b5691a;--ok:#2c7a4b;--brand:#3a5a78}
*{box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--soft);margin:0;line-height:1.62;font-size:16px}
.wrap{max-width:920px;margin:0 auto;padding:48px 28px 90px;background:var(--bg)}
h1{font-size:30px;line-height:1.2;margin:.2em 0 .1em;letter-spacing:-.4px}
h2{font-size:22px;margin:1.9em 0 .5em;padding-bottom:.28em;border-bottom:2px solid var(--line)}
h3{font-size:17px;margin:1.5em 0 .4em;color:var(--brand)}
h4{font-size:15px;margin:1.2em 0 .3em;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
p,li{color:#23282d}
a{color:var(--brand);text-decoration:none;border-bottom:1px solid #cfd8e3}
a:hover{border-bottom-color:var(--brand)}
hr{border:none;border-top:1px solid var(--line);margin:2em 0}
table{border-collapse:collapse;width:100%;margin:1.1em 0;font-size:14.5px}
th,td{border:1px solid var(--line);padding:8px 11px;text-align:left;vertical-align:top}
th{background:var(--accent);color:#fff;font-weight:600}
tr:nth-child(even) td{background:var(--soft)}
code{background:var(--soft);padding:1px 5px;border-radius:4px;font-size:13.5px;color:#b5310a}
blockquote{margin:1.2em 0;padding:.5em 1.1em;border-left:3px solid var(--brand);background:var(--soft);color:var(--muted);font-size:14.5px}
strong{color:#12161a}
.wrap>p:first-of-type{color:var(--muted)}
ul,ol{padding-left:1.35em}
li{margin:.28em 0}
</style>
"""
html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title><style>{CSS}</head><body><div class="wrap">{body}</div></body></html>"""
with open(html_path,'w',encoding='utf-8') as f:
    f.write(html)
print("Wrote", html_path, "(", len(html), "bytes )")
