"""Build design/type-sample.html (the live index.html plus three type changes) and
design/type-compare.html (current vs sample, desktop and phone, side by side).
Run from the repo root after `git pull`, so the sample always starts from the latest site:
    python3 tools/build_type_sample.py
Handwritten first letters: fonts/hand-*-subset.woff2 (Zhi Mang Xing, Long Cang, Pinyon Script; OFL, see fonts/hand-fonts-OFL.txt).
"""
import os

s = open('index.html', encoding='utf-8').read()
s = s.replace('href="fonts/', 'href="../fonts/').replace("'art/logos/", "'../art/logos/").replace('"art/logos/', '"../art/logos/')
css = '''<style id="type-sample">
/* 手写首字：每个大标题的第一个字换成手写体（学 Every 的 hand 首字母）。中文用行书，英文模式用花体大写。
   用 ::first-letter，不改 DOM，就地翻译照常工作；新写的标题自动套用。字体均为 OFL，按站内用字子集化。 */
@font-face{font-family:"HandZh";src:url("../fonts/hand-zhimangxing-subset.woff2") format("woff2");font-display:swap}
@font-face{font-family:"HandZh2";src:url("../fonts/hand-longcang-subset.woff2") format("woff2");font-display:swap}
@font-face{font-family:"HandLatin";src:url("../fonts/hand-pinyonscript-subset.woff2") format("woff2");font-display:swap}
:root{--hand:"HandLatin","HandZh",var(--serif)} html.hand-longcang{--hand:"HandLatin","HandZh2",var(--serif)}
:is(.hero .h,.page-head .display,.sec .hd h3.serif,.h2,.faq h2,.cta-end .display,.feat .it b,.prod b,.card h3,.case b,.detail .display,.article h1,.coop h2.display)::first-letter{font-family:var(--hand);font-weight:400;font-size:1.3em;line-height:1;letter-spacing:0;padding-right:.05em}
html[lang="en"] :is(.hero .h,.page-head .display,.sec .hd h3.serif,.h2,.faq h2,.cta-end .display,.feat .it b,.prod b,.card h3,.case b,.detail .display,.article h1,.coop h2.display)::first-letter{font-size:1.3em;padding-right:.02em}
</style>
<script>if(/hand=longcang/.test(location.search))document.documentElement.classList.add('hand-longcang')</script>
'''
i = s.find('</head>'); assert i > 0
s = s[:i] + css + s[i:]
os.makedirs('design', exist_ok=True)
open('design/type-sample.html', 'w', encoding='utf-8').write(s)

cmp = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>字体样张对比</title>
<style>
:root{--paper:#F8F8F8;--ink:#000;--ink50:rgba(0,0,0,.5);--line:rgba(0,0,0,.1)}
html,body{margin:0;background:var(--paper);color:var(--ink);font:400 15px/1.6 "DM Sans","PingFang SC",system-ui,sans-serif}
.wrap{max-width:1480px;margin:0 auto;padding:28px 16px 60px}
h1{font:400 30px/1.1 Georgia,"Songti SC",serif;letter-spacing:-.02em;margin:0 0 6px}
p.lead{margin:0 0 4px;color:rgba(0,0,0,.7);max-width:80ch}
ul{margin:6px 0 18px;padding-left:18px;color:rgba(0,0,0,.7)} li{margin:2px 0}
.k{font:400 11px ui-monospace,Menlo,monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--ink50);margin:0 0 6px}
.row{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:18px}
.frame{background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.05)}
.desk{position:relative;width:100%;aspect-ratio:1440/900;overflow:hidden}
.desk iframe{position:absolute;left:0;top:0;width:1440px;height:900px;border:0;transform-origin:0 0}
.phones{display:flex;gap:20px;justify-content:center;flex-wrap:wrap;margin-top:22px}
.phone .frame{border-radius:28px} .ph{position:relative;width:300px;height:650px;overflow:hidden}
.ph iframe{position:absolute;left:0;top:0;width:390px;height:845px;border:0;transform:scale(.769);transform-origin:0 0}
.tabs{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}
.tabs button{appearance:none;border:1px solid var(--line);background:#fff;border-radius:999px;padding:6px 14px;font:inherit;font-size:13px;cursor:pointer}
.tabs button.on{background:#000;color:#fff;border-color:#000}
@media (max-width:820px){.row{grid-template-columns:1fr}}
</style></head><body><div class="wrap">
<div class="k">样张 · 2026-10-13</div>
<h1>字体样张：手写首字</h1>
<p class="lead">左边是线上现版，右边是样张。样张只改一处：每个大标题的第一个字换成手写体，中文用行书，切到 EN 时用花体大写。其余不变。</p>
<div class="tabs" id="hand"><button class="on" data-h="">志莽行书</button><button data-h="?hand=longcang">龙藏体</button></div>
<div class="tabs" id="tabs" style="margin-top:8px"><button class="on" data-r="home">首页</button><button data-r="models">产品与服务</button><button data-r="news">新闻动态</button><button data-r="about">关于</button></div>
<div class="row">
 <div><div class="k">现版</div><div class="frame desk"><iframe id="a" src="../index.html#home"></iframe></div></div>
 <div><div class="k">样张</div><div class="frame desk"><iframe id="b" src="type-sample.html#home"></iframe></div></div>
</div>
<div class="phones">
 <div class="phone"><div class="k">现版 · 手机</div><div class="frame ph"><iframe id="c" src="../index.html#home"></iframe></div></div>
 <div class="phone"><div class="k">样张 · 手机</div><div class="frame ph"><iframe id="d" src="type-sample.html#home"></iframe></div></div>
</div>
</div>
<script>
function fit(){document.querySelectorAll('.desk').forEach(function(d){d.querySelector('iframe').style.transform='scale('+(d.clientWidth/1440)+')'})}
addEventListener('resize',fit);fit();
var R='home',Q='';
function load(){['a','c'].forEach(function(id){document.getElementById(id).src='../index.html#'+R});['b','d'].forEach(function(id){document.getElementById(id).src='type-sample.html'+Q+'#'+R})}
document.querySelectorAll('#tabs button').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('#tabs button').forEach(function(x){x.classList.toggle('on',x===b)});R=b.dataset.r;load()})});
document.querySelectorAll('#hand button').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('#hand button').forEach(function(x){x.classList.toggle('on',x===b)});Q=b.dataset.h;load()})});
</script></body></html>
'''
open('design/type-compare.html', 'w', encoding='utf-8').write(cmp)
print('written design/type-sample.html, design/type-compare.html')
