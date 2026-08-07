"""Render docs/final_report.md -> outputs/final_report.html with the water-balance figure embedded."""
import markdown, base64, sys
md = open("docs/final_report.md", encoding="utf-8").read()
body = markdown.markdown(md, extensions=["tables","fenced_code","attr_list","sane_lists"])
# embed the water-balance figure as base64
b64 = base64.b64encode(open("outputs/fig_water_balance.png","rb").read()).decode()
body = body.replace('src="WBFIG"', f'src="data:image/png;base64,{b64}" style="width:100%;border:1px solid #e3e7ec;border-radius:6px;margin:10px 0"')
CSS = """
:root{--ink:#1a1d21;--mut:#5b6570;--line:#e3e7ec;--bg:#fff;--soft:#f6f8fa;--accent:#2c5f4f;--brand:#3a5a78}
*{box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:var(--ink);background:var(--soft);margin:0;line-height:1.62;font-size:16px}
.wrap{max-width:940px;margin:0 auto;padding:44px 26px 90px;background:var(--bg)}
h1{font-size:29px;margin:.15em 0;letter-spacing:-.4px}h2{font-size:21px;margin:1.7em 0 .5em;padding-bottom:.28em;border-bottom:2px solid var(--line)}
h3{font-size:16.5px;margin:1.4em 0 .35em;color:var(--brand)}
p,li{color:#23282d}a{color:var(--brand)}
blockquote{margin:1.1em 0;padding:.5em 1em;border-left:3px solid var(--accent);background:var(--soft);color:var(--mut);font-size:14px}
table{border-collapse:collapse;width:100%;margin:1.1em 0;font-size:13.6px}
th,td{border:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top}
th{background:var(--accent);color:#fff;font-weight:600}tr:nth-child(even) td{background:var(--soft)}
code{background:var(--soft);padding:1px 5px;border-radius:4px;font-size:13px;color:#b5310a}
strong{color:#12161a}hr{border:none;border-top:1px solid var(--line);margin:1.8em 0}
ul,ol{padding-left:1.35em}li{margin:.25em 0}
"""
html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Retirement Hacienda — Site Selection Analysis</title><style>{CSS}</style></head><body><div class="wrap">{body}</div></body></html>"""
open("outputs/final_report.html","w",encoding="utf-8").write(html)
print("Saved outputs/final_report.html", round(len(html)/1000,1), "KB")
