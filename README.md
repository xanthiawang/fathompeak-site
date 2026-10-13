# 沐仞官网原型（可部署版）

线上地址：https://xanthiawang.github.io/fathompeak-site/ （GitHub Pages，main 分支根目录；推送后约一分钟生效）

- `index.html`：整站单文件（hash 路由：#home #models #enterprise #network #news #docs #about #login #console …）。
- `art/logos/`：合作带的 logo 图片，`index.html` 以相对路径引用。
- 改文案：直接编辑 `index.html`。页面文字在各 `<section data-route="…">` 里；模型、节点、看板行、评价在脚本区 `var M= / var T= / var N= / var R=`；英文在 `var I18N={…}`。
- 发布：把本目录推到 GitHub 仓库，Settings → Pages → 选 main 分支根目录，即可得到公开地址；也可直接拖进 Netlify / Vercel。
- 数据来源：模型目录与输出参考价于 2026-10-13 对照 admin.fathompeak.cn/token-market 的公开页面，共 7 个模型；DeepSeek 价格对应空闲时段，MiniMax-M3 价格对应 ≤512k 档。节点、交易行和评价保留既有采集内容；不代表当前运行状态。控制台数字为原有界面展示内容，不代表真实账户账单。指南用于接入与采购准备；更新日志与周报没有已发布内容。


## 2026-10-13 中文文案与流程核对

- 重写首页、产品、企业采购、节点合作、公司介绍、接入文档、九篇指南及交互提示，按公司资料区分三类产品与节点运营合作。
- 原样保留所有 CSS、inline styles、字体文件、图像、配色及组件布局。通过缩短文字处理手机端宽度。
- 首页和底部统一为“获取 API Key / 申请成为产地”，接入指南置于下方。模型、账户、文档和合作入口均使用本站路由，不再跳转旧平台。当前控制台、账户步骤和模型调用仍为交互预览，不创建账户、密钥或模型回复。
- 联系与订阅表单未接通提交服务，点击不会上传信息；商务需求通过公开邮箱联系。PDF、视频、图片下载、社交账号与协议入口以当前提示为准，待补正式材料。
- 修正产品卡片及页脚跨页面定位、同一 hash 下控制台预览跳转、未收录模型的处理和代码复制时夹带按钮文字的问题。示例使用待替换的 HTTPS 接入域名；按正式接口文档填写后再调用。
- 核查桌面 1440 × 900 和手机 390 × 844 的主路由、全部模型详情与九篇指南；新版无横向页面溢出。JavaScript 语法检查和 git diff --check 通过。
- 中文为完整主文案。关键英文提示已同步；未完成翻译的正文保留中文，避免逐词替换造成混杂或恢复旧承诺。
- 浏览器内复制按钮回调与代码内容已核查；内置浏览器的剪贴板读取未返回内容，本次未确认系统剪贴板实际写入。

## 编辑与同步（2026-10-13 起）

- 这个仓库是官网的唯一源文件。查看：https://xanthiawang.github.io/fathompeak-site/ ；编辑：https://github.com/xanthiawang/fathompeak-site 。
- 改哪里：整站都在 `index.html`；logo 在 `art/logos/`，字体在 `fonts/`。推送到 main 约 1 分钟后线上自动更新，大家看到的永远是最新版。
- 网页上直接改：打开 `index.html` → 右上角铅笔 → 修改 → Commit changes。本地改：`git pull` → 改 → `git commit` → `git push`。改之前先 pull，避免覆盖别人的修改。
- 编辑权限：仓库 Settings → Collaborators → Add people，输入对方的 GitHub 用户名。
- `design/`：设计交付文档（`handoff-deck.pdf` / `.pptx`）和色卡与字体页（线上 `design/palette-type.html`）。
- `tools/`：重拍交付文档截图、重建交付文档的脚本（路径按 Zixin 本机写）。
- 境内稳定访问：把仓库内容放到公司已备案域名的网站根目录。
