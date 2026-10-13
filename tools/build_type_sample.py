"""Build design/type-sample.html (the live index.html plus three type changes) and
design/type-compare.html (current vs sample, desktop and phone, side by side).
Run from the repo root after `git pull`, so the sample always starts from the latest site:
    python3 tools/build_type_sample.py
The pixel font subset lives in fonts/fusion-pixel-12px-subset.woff2 (Fusion Pixel, OFL, see fonts/fusion-pixel-OFL.txt).
"""
import os

s = open('index.html', encoding='utf-8').read()
s = s.replace('href="fonts/', 'href="../fonts/').replace("'art/logos/", "'../art/logos/").replace('"art/logos/', '"../art/logos/')
a = '<p class="h" role="heading" aria-level="1">主流模型 <span class="x">×</span> 异构算力，'
assert s.count(a) == 1, 'hero headline changed; update the marker'
s = s.replace(a, '<p class="h" role="heading" aria-level="1">主流模型 <span class="x">×</span> <span class="px">异构算力</span>，')
css = '''<style id="type-sample">
@font-face{font-family:"FusionPixel";src:url("../fonts/fusion-pixel-12px-subset.woff2") format("woff2");font-display:swap}
/* 1 点阵：首屏只有「异构算力」用 12px 点阵字的整数倍（桌面 36px = 3 倍，手机 24px = 2 倍），像素边缘才清楚 */
.hero .h .px{font-family:"FusionPixel",var(--serif);font-size:36px;letter-spacing:.04em;font-weight:400;color:rgba(255,255,255,.9);-webkit-font-smoothing:none;text-rendering:optimizeSpeed}
@media (max-width:800px){.hero .h .px{font-size:24px}}
/* 2 标题收紧：行高约 1.0，字距 -0.04em */
.hero .h,.page-head .display,.cta-end .display,.h2,.faq h2,.sec .hd h3.serif,.pdet .hd h3,.prod b{line-height:1.02;letter-spacing:-.04em}
@media (max-width:800px){.hero .h{line-height:1.1}}
/* 3 新闻与公司页：旧式数字 */
.ev,.events,.news,section[data-route="about"]{font-variant-numeric:oldstyle-nums proportional-nums}
</style>
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
<h1>字体样张：点阵字与收紧标题</h1>
<p class="lead">左边是线上现版，右边是样张。样张只改三处，其余不变：</p>
<ul><li>首屏「异构算力」换成开源点阵字 Fusion Pixel（OFL），桌面 36px、手机 24px，都是 12px 点阵的整数倍。</li>
<li>首屏、区块和页面大标题行高收到约 1.0，字距 −0.04em。</li>
<li>新闻与关于页用旧式数字。</li></ul>
<div class="tabs" id="tabs"><button class="on" data-r="home">首页</button><button data-r="models">产品与服务</button><button data-r="news">新闻动态</button><button data-r="about">关于</button></div>
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
document.querySelectorAll('#tabs button').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('#tabs button').forEach(function(x){x.classList.toggle('on',x===b)});var r=b.dataset.r;
 ['a','c'].forEach(function(id){document.getElementById(id).src='../index.html#'+r});['b','d'].forEach(function(id){document.getElementById(id).src='type-sample.html#'+r})})});
</script></body></html>
'''
open('design/type-compare.html', 'w', encoding='utf-8').write(cmp)
print('written design/type-sample.html, design/type-compare.html')
