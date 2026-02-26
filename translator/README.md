# 在线翻译工具

这是一个基于 Flask 和 Google Translate API 的简单在线翻译工具。

## 功能特性

- 支持多种语言之间的互译
- 自动检测源语言
- 响应式网页界面
- 实时翻译结果展示

## 支持的语言

- 中文 (zh)
- 英语 (en)
- 日语 (ja)
- 韩语 (ko)
- 法语 (fr)
- 德语 (de)
- 西班牙语 (es)
- 俄语 (ru)
- 阿拉伯语 (ar)
- 意大利语 (it)
- 葡萄牙语 (pt)
- 印地语 (hi)

## 安装和运行

1. 克隆项目到本地
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行应用：
   ```bash
   python app.py
   ```
4. 在浏览器中访问 `http://localhost:5000`

## 技术栈

- 后端：Python Flask
- 前端：HTML/CSS/JavaScript
- 翻译API：Google Translate API (免费接口)

## 注意事项

- 此项目使用的是 Google Translate 的免费接口，可能会有调用频率限制
- 请勿用于商业用途，仅限学习交流