# 沐仞官网原型（可部署版）

- `index.html`：整站单文件（hash 路由：#home #models #enterprise #network #news #docs #about #login #console …）。
- `art/logos/`：合作带的 logo 图片，`index.html` 以相对路径引用。
- 改文案：直接编辑 `index.html`。页面文字在各 `<section data-route="…">` 里；模型、节点、看板行、评价在脚本区 `var M= / var T= / var N= / var R=`；英文在 `var I18N={…}`。
- 发布：把本目录推到 GitHub 仓库，Settings → Pages → 选 main 分支根目录，即可得到公开地址；也可直接拖进 Netlify / Vercel。
- 数据来源：模型、节点、看板行、评价取自 test.admin.fathompeak.cn 2026-10-12 / 10-13 的公开页面；指南、更新日志、周报为内容设计，上线前替换。
