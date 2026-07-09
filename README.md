# 林寸的个人博客

🔗 **线上地址：** https://lincun.linjie.online

一个简约、高级感的个人博客，用于展示创作项目和技术探索。

## ✨ 特性

- 🌑 暗色主题 + 光晕背景动画
- 🖱️ 鼠标跟随光效 + 卡片 3D 倾斜
- ⌨️ Hero 区打字机效果
- 📱 响应式设计 + 移动端汉堡菜单
- 🧭 固定导航栏（滚动毛玻璃效果）
- 🔒 HTTPS + HTTP/2

## 🛠️ 技术栈

| 技术 | 用途 |
|------|------|
| [Astro 7](https://astro.build) | 静态站点生成 |
| [Tailwind CSS v4](https://tailwindcss.com) | 样式系统 |
| [GSAP](https://greensock.com/gsap/) | 动画引擎 |
| Nginx | 反向代理 + HTTPS |
| 阿里云 Ubuntu 24.04 | 服务器 |

## 📂 项目结构

```
blog/
├── src/
│   ├── layouts/
│   │   └── Base.astro          # 基础布局（导航栏 + 移动端菜单 + 光效）
│   ├── pages/
│   │   ├── index.astro         # 首页（Hero + 关于 + 技术栈 + 项目 + 时间线 + 动态）
│   │   └── projects/
│   │       ├── history.astro   # 历史科普系列
│   │       ├── ue5.astro       # UE5 修仙 RPG
│   │       ├── mc.astro        # MC 修仙服
│   │       └── comfyui.astro   # ComfyUI 人物管线
│   └── styles/
│       └── global.css          # Tailwind 入口
├── public/
│   ├── favicon.ico
│   └── favicon.svg
├── astro.config.mjs            # Astro 配置
├── package.json
└── tsconfig.json
```

## 🚀 本地开发

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览构建结果
npm run preview
```

## 📦 部署

```bash
# 构建
npm run build

# 一键部署到服务器（需要 deploy.py，不包含在仓库中）
python deploy.py
```

## 📝 内容页面

- **首页** — Hero 动画 + 关于我 + 技术栈 + 项目卡片 + 时间线 + 最近动态
- **历史科普** — 说书人叙事风格，成语溯源，知识包裹
- **UE5 修仙 RPG** — 虚幻引擎 5，蓝图 + EnhancedInput + StateTree
- **MC 修仙服** — Paper 1.21.4，四件套自研插件，双币经济系统
- **ComfyUI 人物管线** — 国漫数字插画风格，IPAdapter + ControlNet

## 📄 License

MIT
