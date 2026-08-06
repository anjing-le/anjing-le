#!/usr/bin/env python3
"""Generate the hand-drawn, animated SVG system used by the profile README."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANIMATED = ROOT / "assets" / "animated"
CARDS = ANIMATED / "project-cards"

INK = "#111827"
PAPER = "#fffdf7"

COMMON_STYLE = """
  <style>
    .hand{font-family:"Comic Sans MS","Chalkboard SE","PingFang SC","Microsoft YaHei",ui-sans-serif,sans-serif}
    .line{fill:none;stroke:#111827;stroke-width:5;stroke-linecap:round;stroke-linejoin:round}
    .soft-line{fill:none;stroke:#111827;stroke-width:3.5;stroke-linecap:round;stroke-linejoin:round}
    .flow{stroke-dasharray:7 9;animation:flow 1.8s linear infinite}
    .bob{animation:bob 2.4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
    .pulse{animation:pulse 1.8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
    .blink{animation:blink 1.1s steps(2,end) infinite}
    .orbit{animation:orbit 7s linear infinite;transform-box:fill-box;transform-origin:center}
    .draw{stroke-dasharray:64;stroke-dashoffset:64;animation:draw 2.6s ease-in-out infinite}
    .bar1,.bar2,.bar3{transform-box:fill-box;transform-origin:center bottom;animation:grow 2.4s ease-in-out infinite}
    .bar2{animation-delay:.22s}.bar3{animation-delay:.44s}
    @keyframes flow{to{stroke-dashoffset:-32}}
    @keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
    @keyframes pulse{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.14);opacity:.72}}
    @keyframes blink{0%,45%{opacity:1}46%,100%{opacity:.15}}
    @keyframes orbit{to{transform:rotate(360deg)}}
    @keyframes draw{0%,18%{stroke-dashoffset:64}55%,88%{stroke-dashoffset:0}100%{stroke-dashoffset:-64}}
    @keyframes grow{0%,100%{transform:scaleY(.45)}50%{transform:scaleY(1)}}
    @media(prefers-reduced-motion:reduce){.flow,.bob,.pulse,.blink,.orbit,.draw,.bar1,.bar2,.bar3{animation:none!important}}
  </style>
"""


def terminal_icon(accent: str, tint: str) -> str:
    return f"""
    <rect x="2" y="7" width="151" height="112" rx="15" fill="{PAPER}" class="line"/>
    <path d="M3 36H152" class="soft-line"/><circle cx="20" cy="22" r="5" fill="{accent}"/><circle cx="37" cy="22" r="5" fill="#f3c969"/><circle cx="54" cy="22" r="5" fill="#79b36a"/>
    <path d="M21 59l14 12-14 12M44 83h31" class="line"/>
    <rect x="93" y="54" width="36" height="25" rx="6" fill="{tint}" stroke="{accent}" stroke-width="4" class="bob"/>
    <rect x="105" y="91" width="36" height="25" rx="6" fill="{accent}" fill-opacity=".2" stroke="{accent}" stroke-width="4" class="bob" style="animation-delay:.35s"/>
    <path d="M82 71h8M90 71v31h11" stroke="{accent}" stroke-width="4" stroke-linecap="round" stroke-dasharray="4 7" class="flow"/>
    <rect x="77" y="82" width="5" height="19" rx="2" fill="{accent}" class="blink"/>
    """


def platform_icon(accent: str, tint: str) -> str:
    return f"""
    <rect x="16" y="7" width="130" height="105" rx="15" fill="{PAPER}" class="line"/>
    <path d="M17 35H145" class="soft-line"/><circle cx="33" cy="21" r="4.5" fill="{accent}"/><circle cx="49" cy="21" r="4.5" fill="#f3c969"/>
    <rect x="34" y="51" width="42" height="42" rx="10" fill="{tint}" stroke="{accent}" stroke-width="4"/>
    <circle cx="55" cy="72" r="8" fill="{accent}" class="pulse"/>
    <path d="M76 72H95M116 51V42M116 93v11" stroke="{accent}" stroke-width="4" stroke-linecap="round" stroke-dasharray="5 7" class="flow"/>
    <rect x="96" y="47" width="39" height="21" rx="7" fill="#e9f8ef" stroke="{INK}" stroke-width="4"/>
    <rect x="96" y="77" width="39" height="21" rx="7" fill="#fff4db" stroke="{INK}" stroke-width="4"/>
    <path d="M3 125c34-8 116-7 159 0" stroke="{accent}" stroke-width="5" stroke-linecap="round"/>
    """


def api_icon(accent: str, tint: str) -> str:
    return f"""
    <circle cx="16" cy="65" r="9" fill="{accent}" class="pulse"/>
    <path d="M28 65H57" stroke="{accent}" stroke-width="5" stroke-linecap="round" class="flow"/>
    <path d="M60 24L98 38V93L60 107Z" fill="{tint}" class="line"/>
    <path d="M78 47v37" stroke="{accent}" stroke-width="5" stroke-linecap="round"/>
    <path d="M98 65h25M123 65V28M123 65v38" stroke="{accent}" stroke-width="4" stroke-linecap="round" stroke-dasharray="6 7" class="flow"/>
    <rect x="119" y="10" width="42" height="29" rx="8" fill="{PAPER}" class="soft-line"/><rect x="119" y="51" width="42" height="29" rx="8" fill="{PAPER}" class="soft-line"/><rect x="119" y="92" width="42" height="29" rx="8" fill="{PAPER}" class="soft-line"/>
    <circle cx="140" cy="24" r="5" fill="{accent}"/><circle cx="140" cy="65" r="5" fill="#79b36a"/><circle cx="140" cy="106" r="5" fill="#f3c969"/>
    """


def auth_icon(accent: str, tint: str) -> str:
    return f"""
    <rect x="3" y="14" width="92" height="107" rx="14" fill="{PAPER}" class="line"/>
    <circle cx="49" cy="49" r="18" fill="{tint}" stroke="{accent}" stroke-width="4"/>
    <path d="M25 95c7-20 42-20 49 0" class="line"/>
    <path d="M94 69h18" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/>
    <g class="bob"><rect x="107" y="56" width="54" height="58" rx="12" fill="{tint}" class="line"/><path d="M121 57V43c0-27 33-27 33 0v14" class="line"/><circle cx="134" cy="81" r="6" fill="{accent}"/><path d="M134 86v12" stroke="{accent}" stroke-width="5" stroke-linecap="round"/></g>
    <path d="M116 124l10 10 25-28" stroke="{accent}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" class="draw"/>
    """


def llm_icon(accent: str, tint: str) -> str:
    return f"""
    <path d="M4 45h39l12 11-12 11H4c-8 0-8-22 0-22Z" fill="{PAPER}" class="soft-line"/><path d="M16 56h22" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    <path d="M55 56H76" stroke="{accent}" stroke-width="4" class="flow"/>
    <circle cx="91" cy="56" r="20" fill="{tint}" class="line"/><path d="M83 56h16M91 48v16" stroke="{accent}" stroke-width="4" stroke-linecap="round" class="pulse"/>
    <path d="M111 56h17M128 56V19M128 56v37" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/>
    <rect x="124" y="2" width="39" height="29" rx="9" fill="#fff4ee" class="soft-line"/><rect x="124" y="42" width="39" height="29" rx="9" fill="#f3faef" class="soft-line"/><rect x="124" y="82" width="39" height="29" rx="9" fill="#f4f1ff" class="soft-line"/>
    <text class="hand" x="135" y="22" font-size="13" font-weight="900" fill="{INK}">A</text><text class="hand" x="135" y="62" font-size="13" font-weight="900" fill="{INK}">B</text><text class="hand" x="135" y="102" font-size="13" font-weight="900" fill="{INK}">C</text>
    <path d="M26 126h114" stroke="{accent}" stroke-width="5" stroke-linecap="round"/><circle cx="55" cy="126" r="7" fill="#f3c969" class="pulse"/><circle cx="104" cy="126" r="7" fill="{accent}" class="pulse" style="animation-delay:.45s"/>
    """


def skill_icon(accent: str, tint: str) -> str:
    return f"""
    <g class="orbit">
      <rect x="4" y="8" width="45" height="34" rx="9" fill="#fff4ee" class="soft-line"/><path d="M18 25h17" stroke="#e98263" stroke-width="4" stroke-linecap="round"/>
      <rect x="112" y="9" width="45" height="34" rx="9" fill="#f4f1ff" class="soft-line"/><path d="M127 18l16 16M143 18l-16 16" stroke="#8975ff" stroke-width="4" stroke-linecap="round"/>
      <rect x="58" y="101" width="45" height="34" rx="9" fill="#eef6ff" class="soft-line"/><circle cx="80" cy="118" r="8" fill="#5b8def"/>
    </g>
    <path d="M36 40L65 66M125 40L97 66M80 101V91" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/>
    <rect x="48" y="49" width="65" height="51" rx="14" fill="{tint}" class="line"/>
    <path d="M64 66h33M64 80h22" stroke="{accent}" stroke-width="5" stroke-linecap="round"/>
    <circle cx="105" cy="94" r="8" fill="#f3c969" class="pulse"/>
    """


def aigc_icon(accent: str, tint: str) -> str:
    return f"""
    <path d="M6 66h35" stroke="{accent}" stroke-width="5" stroke-linecap="round" class="flow"/><path d="M13 51l6 10 11 3-10 6-3 11-6-10-11-3 10-6Z" fill="#f3c969" class="pulse"/>
    <path d="M43 22h70v86H43Z" fill="{PAPER}" class="line"/>
    <path d="M54 80l16-20 13 14 11-12 10 22H54Z" fill="{tint}" stroke="{accent}" stroke-width="3" stroke-linejoin="round"/><circle cx="92" cy="45" r="8" fill="#f3c969"/>
    <g class="bob"><rect x="99" y="49" width="58" height="70" rx="9" fill="#f4f1ff" class="line"/><path d="M112 68h31M112 82h25M112 96h34" stroke="{accent}" stroke-width="4" stroke-linecap="round"/></g>
    <path d="M117 16l5 10 11 5-11 5-5 11-5-11-11-5 11-5Z" fill="{accent}" class="pulse"/>
    """


def knowledge_icon(accent: str, tint: str) -> str:
    return f"""
    <path d="M3 18h60v78H3Z" fill="{PAPER}" class="line"/><path d="M14 38h37M14 54h31M14 70h35" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    <path d="M64 57h26" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/>
    <g class="pulse"><circle cx="101" cy="42" r="8" fill="{accent}"/><circle cx="89" cy="65" r="7" fill="#f3c969"/><circle cx="111" cy="71" r="7" fill="#8975ff"/><path d="M96 49l-4 10M106 49l3 15M96 67l8 2" stroke="{INK}" stroke-width="3"/></g>
    <path d="M118 61h12" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/>
    <path d="M126 39h35v54h-24l-12 12 3-12h-2Z" fill="{tint}" class="line"/><path d="M139 55h12M139 68h9" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    <circle cx="154" cy="101" r="10" fill="{accent}" class="pulse"/><path d="M150 101l3 3 6-8" stroke="white" stroke-width="3" fill="none" stroke-linecap="round"/>
    """


def service_icon(accent: str, tint: str) -> str:
    return f"""
    <path d="M7 20h91v64H49L32 99l4-15H7Z" fill="{tint}" class="line"/>
    <circle cx="32" cy="53" r="5" fill="{accent}" class="pulse"/><circle cx="51" cy="53" r="5" fill="{accent}" class="pulse" style="animation-delay:.2s"/><circle cx="70" cy="53" r="5" fill="{accent}" class="pulse" style="animation-delay:.4s"/>
    <path d="M98 57h19" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/>
    <g class="bob"><circle cx="138" cy="51" r="22" fill="#ffe8c7" class="soft-line"/><path d="M119 50v-5c0-26 38-26 38 0v8" class="line"/><rect x="112" y="45" width="10" height="24" rx="5" fill="{accent}"/><rect x="154" y="45" width="10" height="24" rx="5" fill="{accent}"/><path d="M158 69c-3 11-12 15-22 15" class="soft-line"/><circle cx="133" cy="84" r="4" fill="{accent}"/></g>
    <path d="M19 119c29-8 105-7 143 0" stroke="{accent}" stroke-width="5" stroke-linecap="round"/>
    """


def order_icon(accent: str, tint: str) -> str:
    return f"""
    <path d="M5 10h64v105l-8-6-8 6-8-6-8 6-8-6-8 6-8-6-8 6Z" fill="{PAPER}" class="line"/><path d="M18 34h37M18 51h28M18 68h36" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    <path d="M70 62h22" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/>
    <g class="orbit"><path d="M105 42l8-7 8 7 10-1 3 10 8 6-5 9 1 10-10 4-6 8-9-5-10 3-5-9-9-5 3-10-3-10 9-5 7-5Z" fill="{tint}" class="soft-line"/><circle cx="115" cy="62" r="12" fill="{accent}"/></g>
    <path d="M137 79h22" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/>
    <circle cx="145" cy="105" r="22" fill="#e9f8ef" class="line"/><path d="M134 105l8 8 15-20" stroke="#3b9a63" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round" class="draw"/>
    """


def analyst_icon(accent: str, tint: str) -> str:
    return f"""
    <rect x="3" y="17" width="58" height="42" rx="10" fill="{tint}" class="line"/><text class="hand" x="16" y="45" fill="{accent}" font-size="18" font-weight="900">SQL</text>
    <path d="M62 39h25" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/>
    <rect x="82" y="7" width="79" height="108" rx="12" fill="{PAPER}" class="line"/>
    <path d="M95 95h53M99 82V64M117 82V42M135 82V27" stroke="{accent}" stroke-width="12" stroke-linecap="round"/>
    <rect class="bar1" x="93" y="62" width="12" height="21" rx="5" fill="{accent}"/><rect class="bar2" x="111" y="40" width="12" height="43" rx="5" fill="#f3c969"/><rect class="bar3" x="129" y="25" width="12" height="58" rx="5" fill="#79b36a"/>
    <path d="M96 104c15-11 28-7 48-22" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/>
    <circle cx="145" cy="82" r="7" fill="{accent}" class="pulse"/>
    """


def finance_icon(accent: str, tint: str) -> str:
    return f"""
    <path d="M3 13h57v91l-7-5-7 5-7-5-7 5-7-5-7 5-7-5-8 5Z" fill="{PAPER}" class="line"/><text class="hand" x="19" y="42" fill="{accent}" font-size="19" font-weight="900">¥</text><path d="M16 58h31M16 73h24" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    <path d="M62 57h35" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/><circle cx="80" cy="57" r="7" fill="#f3c969" class="pulse"/>
    <path d="M98 13h57v91l-7-5-7 5-7-5-7 5-7-5-7 5-7-5-8 5Z" fill="{tint}" class="line"/><text class="hand" x="114" y="42" fill="{accent}" font-size="19" font-weight="900">¥</text><path d="M111 58h31M111 73h24" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    <circle cx="128" cy="111" r="19" fill="#e9f8ef" class="line"/><path d="M119 111l7 7 14-18" stroke="#3b9a63" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round" class="draw"/>
    """


def copilot_icon(accent: str, tint: str) -> str:
    return f"""
    <rect x="4" y="7" width="155" height="111" rx="13" fill="{PAPER}" class="line"/><path d="M5 34h153M56 35v82M107 35v82" class="soft-line"/>
    <rect x="16" y="46" width="28" height="17" rx="5" fill="#dbeafe" stroke="{accent}" stroke-width="3"/><rect x="68" y="47" width="27" height="26" rx="5" fill="#fff4db" stroke="#e6a23c" stroke-width="3" class="bob"/><rect x="119" y="47" width="27" height="36" rx="5" fill="#e9f8ef" stroke="#3b9a63" stroke-width="3"/>
    <path d="M29 64v22h51" stroke="{accent}" stroke-width="4" stroke-dasharray="5 7" class="flow"/><path d="M80 82l-7-6M80 82l-7 6" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    <circle cx="81" cy="96" r="8" fill="{accent}" class="pulse"/><path d="M122 100l7 7 15-18" stroke="#3b9a63" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round" class="draw"/>
    """


def voice_icon(accent: str, tint: str) -> str:
    return f"""
    <path d="M3 9h91c9 0 16 7 16 16v47c0 9-7 16-16 16H48L30 102l4-14H3c-9 0-16-7-16-16V25C-13 16-6 9 3 9Z" fill="{PAPER}" class="line"/>
    <circle cx="11" cy="49" r="6" fill="{accent}" class="pulse"/>
    <path d="M27 49h8M43 39v20M53 30v38M63 42v14M73 35v28M83 42v14M93 49h7" stroke="{accent}" stroke-width="5" stroke-linecap="round" class="pulse"/>
    <path d="M112 55c12 0 21 5 29 15" stroke="{accent}" stroke-width="5" stroke-linecap="round" stroke-dasharray="6 7" class="flow"/><path d="M132 65l10 7-8 10" stroke="{accent}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <g class="bob"><path d="M93 80h52l16 16v45H93Z" fill="{PAPER}" class="line"/><path d="M145 80v16h16" class="line"/><path d="M108 106h36M108 121h29" stroke="{accent}" stroke-width="5" stroke-linecap="round"/></g>
    """


def scribe_icon(accent: str, tint: str) -> str:
    return f"""
    <rect x="3" y="7" width="151" height="119" rx="15" fill="{PAPER}" class="line"/><path d="M4 36h149" class="soft-line"/><circle cx="20" cy="22" r="5" fill="#e98263"/><circle cx="37" cy="22" r="5" fill="#f3c969"/><circle cx="54" cy="22" r="5" fill="{accent}"/>
    <rect x="19" y="48" width="24" height="64" rx="7" fill="{tint}"/><path d="M27 62h9M27 76h9M27 90h9" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    <path d="M57 57h59M57 75h48M57 93h66" stroke="#9ca3af" stroke-width="5" stroke-linecap="round"/><rect x="123" y="83" width="4" height="22" rx="2" fill="{accent}" class="blink"/>
    <g class="bob"><path d="M120 105l27-30 14 13-30 27-15 4Z" fill="#ffe8c7" class="line"/><path d="M147 75l14 13" stroke="{accent}" stroke-width="5"/></g>
    """


def bitbun_icon(accent: str, tint: str) -> str:
    return f"""
    <rect x="3" y="18" width="75" height="53" rx="9" fill="{PAPER}" class="line"/><path d="M-6 80h91" class="line"/><circle cx="92" cy="76" r="10" fill="#34d399" class="pulse"/>
    <rect x="114" y="62" width="48" height="52" rx="9" fill="{tint}" class="line"/><path d="M104 121h66" class="line"/>
    <path d="M78 51c18-18 36-18 53 0" stroke="{accent}" stroke-width="7" fill="none" stroke-linecap="round" stroke-dasharray="7 8" class="flow"/><path d="M122 43l11 10-13 8" stroke="{accent}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="103" cy="39" r="6" fill="{accent}" class="bob"/>
    """


CARD_DATA = [
    ("infra-dev-scaffolding", "INFRA · BUILD", "开发脚手架", "前后端 · 契约 · 质量门禁", "#5b8def", "#eef6ff", terminal_icon),
    ("anjing-ai-platform", "INFRA · PLATFORM", "AI 基础设施平台", "Console · Gateway · 权限 · 计费", "#6c78d8", "#f1f2ff", platform_icon),
    ("infra-api-gateway", "INFRA · TRAFFIC", "统一 API 流量入口", "路由 · 限流 · 熔断 · 日志", "#2aa7a0", "#ecfbf8", api_icon),
    ("infra-auth", "INFRA · TRUST", "认证与权限中心", "用户体系 · RBAC · OAuth", "#9a6bd1", "#f7f0ff", auth_icon),
    ("infra-llm-gateway", "INFRA · MODEL", "LLM 算力入口", "多模型调度 · Key 池 · 用量统计", "#398fca", "#ecf8ff", llm_icon),
    ("infra-skill-hub", "INFRA · SKILL", "AI 能力注册中心", "注册 · 发现 · 调度 · 治理", "#4b9d69", "#effaf2", skill_icon),
    ("agent-aigc", "AGENT · CREATE", "全模态创作 Agent", "多模型 · Prompt · 图文音视频", "#e98263", "#fff4ee", aigc_icon),
    ("agent-knowledge", "AGENT · KNOW", "RAG 知识 Agent", "解析 · 向量化 · 检索 · 引用", "#79b36a", "#f3faef", knowledge_icon),
    ("agent-customer-service", "AGENT · SERVE", "智能客服 Agent", "多轮对话 · RAG · 转人工", "#2aa7a0", "#ecfbf8", service_icon),
    ("agent-order-ops", "AGENT · ACT", "订单执行 Agent", "Tool Calling · 审批 · 审计", "#e6a23c", "#fff8e7", order_icon),
    ("agent-data-analyst", "AGENT · ANALYZE", "数据分析 Agent", "Text-to-SQL · 图表 · 洞察", "#8975ff", "#f4f1ff", analyst_icon),
    ("agent-finance-reconcile", "AGENT · REVIEW", "财务对账 Agent", "票据解析 · 规则校验 · 复核", "#e36d7b", "#fff2f3", finance_icon),
    ("agent-project-copilot", "AGENT · CO-OP", "项目协作 Agent", "任务拆解 · 风险 · 周报复盘", "#4d8bd8", "#eef6ff", copilot_icon),
    ("anjing-voicepen", "CREATOR · SPEAK", "开口说 · 自动成文", "AI 润色 · 随处粘贴", "#e98263", "#fff4ee", voice_icon),
    ("anjing-scribe", "CREATOR · WRITE", "沉浸写作 · 本地语音", "Markdown · 可控 AI 修订", "#79b36a", "#f3faef", scribe_icon),
    ("bitbun", "CREATOR · SEND", "文件 · 文字 · 图片", "局域网直达 · 无云端", "#8975ff", "#f4f1ff", bitbun_icon),
]

DISPLAY_NAMES = {
    "anjing-voicepen": "VoicePen",
    "anjing-scribe": "静写 · Scribe",
    "bitbun": "BitBun",
}


def card_svg(slug: str, label: str, subtitle: str, detail: str, accent: str, tint: str, icon_fn) -> str:
    display = DISPLAY_NAMES.get(slug, slug)
    title_size = 25 if len(display) > 21 else 28 if len(display) > 17 else 33
    return f"""<svg width="560" height="220" viewBox="0 0 560 220" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">{display}</title>
  <desc id="desc">{subtitle}；{detail}。右侧动画演示项目的核心工作流。</desc>
{COMMON_STYLE}
  <rect width="560" height="220" rx="24" fill="{PAPER}"/>
  <path d="M29 25C99 18 171 27 244 21C332 14 425 20 532 27C539 79 531 138 536 196C442 203 351 197 274 202C184 207 96 197 29 201C20 142 27 84 29 25Z" fill="{tint}" stroke="{accent}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="51" y="39" width="142" height="25" rx="12.5" fill="{accent}" fill-opacity=".13"/>
  <text class="hand" x="63" y="57" fill="{accent}" font-size="12" font-weight="900" letter-spacing="1">{label}</text>
  <text class="hand" x="56" y="98" fill="{INK}" font-size="{title_size}" font-weight="900">{display}</text>
  <text class="hand" x="56" y="135" fill="#374151" font-size="19" font-weight="800">{subtitle}</text>
  <text class="hand" x="56" y="166" fill="#6b7280" font-size="15.5" font-weight="750">{detail}</text>
  <path d="M56 181c64-5 150 5 231-1" stroke="{accent}" stroke-opacity=".24" stroke-width="3" stroke-linecap="round"/>
  <g transform="translate(375 42)">
{icon_fn(accent, tint)}
  </g>
</svg>
"""


def route_svg() -> str:
    return f"""<svg width="1200" height="340" viewBox="0 0 1200 340" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">Anjing open-source route</title><desc id="desc">从工程底座、Agent 实战、创作者工具到产品落地的开源路线。</desc>
{COMMON_STYLE}
  <rect width="1200" height="340" rx="28" fill="{PAPER}"/>
  <path d="M35 33C192 20 308 38 469 28C631 18 796 26 1160 34C1172 104 1157 235 1165 306C946 320 743 305 576 315C383 327 190 307 39 314C23 220 39 126 35 33Z" fill="#fffaf0" stroke="{INK}" stroke-opacity=".78" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <text class="hand" x="71" y="78" fill="{INK}" font-size="40" font-weight="900">Build → Agent → Create → Ship</text>
  <text class="hand" x="73" y="111" fill="#5b6472" font-size="21" font-weight="800">把基础设施、AI 实战和真实产品放在同一条公开路线里</text>
  <path d="M139 228C327 176 469 235 642 194C802 156 940 196 1080 161" stroke="#9ca3af" stroke-width="5" stroke-linecap="round" stroke-dasharray="10 14" class="flow"/>
  <g transform="translate(75 165)"><g class="bob"><path d="M8 12C28-1 86 2 110 10C113 43 109 88 112 116C72 121 34 114 6 118C0 84 7 47 8 12Z" fill="#eef6ff" stroke="#5b8def" stroke-width="5"/><rect x="26" y="34" width="64" height="48" rx="8" fill="{PAPER}" class="soft-line"/><path d="M27 49h62M39 62l8 7-8 7M55 76h18" stroke="#5b8def" stroke-width="4" fill="none" stroke-linecap="round"/><text class="hand" x="23" y="109" fill="{INK}" font-size="16" font-weight="900">INFRA</text></g></g>
  <g transform="translate(343 146)"><g class="bob" style="animation-delay:.25s"><path d="M5 10C33 2 96 5 124 12C128 47 122 94 126 123C85 128 39 120 6 124C0 87 5 48 5 10Z" fill="#fff2f3" stroke="#e36d7b" stroke-width="5"/><circle cx="65" cy="55" r="25" fill="{PAPER}" class="soft-line"/><path d="M65 33v44M43 55h44" stroke="#e36d7b" stroke-width="5" stroke-linecap="round"/><circle cx="65" cy="55" r="8" fill="#f3c969" class="pulse"/><text class="hand" x="25" y="113" fill="{INK}" font-size="16" font-weight="900">AGENT</text></g></g>
  <g transform="translate(641 125)"><g class="bob" style="animation-delay:.5s"><path d="M7 13C36 3 107 6 137 10C142 50 134 102 139 134C93 141 43 131 7 136C0 96 6 53 7 13Z" fill="#f3faef" stroke="#79b36a" stroke-width="5"/><path d="M29 38h84v56H29Z" fill="{PAPER}" class="soft-line"/><path d="M43 77l16-19 13 12 13-17 16 26H43Z" fill="#d9efcf" stroke="#79b36a" stroke-width="3"/><circle cx="96" cy="50" r="7" fill="#f3c969"/><text class="hand" x="30" y="124" fill="{INK}" font-size="16" font-weight="900">CREATOR</text></g></g>
  <g transform="translate(958 95)"><g class="bob" style="animation-delay:.75s"><path d="M4 11C32 1 101 4 130 10C135 52 128 108 133 143C88 149 42 139 5 144C0 103 4 55 4 11Z" fill="#f4f1ff" stroke="#8975ff" stroke-width="5"/><path d="M28 39h78v61H28Z" fill="{PAPER}" class="soft-line"/><path d="M40 85c13-15 23-9 32-22 8-12 18-4 27-18" stroke="#8975ff" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M90 44h11v12" stroke="#8975ff" stroke-width="4" fill="none"/><text class="hand" x="29" y="130" fill="{INK}" font-size="16" font-weight="900">PRODUCT</text></g></g>
  <circle r="8" fill="#e98263"><animateMotion dur="7s" repeatCount="indefinite" path="M139 228C327 176 469 235 642 194C802 156 940 196 1080 161"/></circle>
</svg>
"""


def products_svg() -> str:
    return f"""<svg width="1200" height="400" viewBox="0 0 1200 400" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">Anjing products</title><desc id="desc">三个长期产品：个人 AI 桌面助手、AIGC 内容工作台和投资监控工具。</desc>
{COMMON_STYLE}
  <rect width="1200" height="400" rx="30" fill="{PAPER}"/>
  <path d="M34 31C196 19 325 38 482 28C650 18 832 27 1161 34C1172 111 1155 276 1164 359C938 375 740 357 571 369C379 382 189 356 38 365C23 247 39 132 34 31Z" fill="#fffaf0" stroke="{INK}" stroke-opacity=".72" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <text class="hand" x="67" y="73" fill="{INK}" font-size="39" font-weight="900">Products grown from real life</text>
  <text class="hand" x="69" y="106" fill="#5b6472" font-size="21" font-weight="800">不是概念 Demo：每一个都从自己的日常系统里长出来</text>
  <g transform="translate(66 135)"><path d="M0 4C72-7 133 5 197 0C245-3 300 2 328 8C335 59 328 174 333 224C254 232 184 221 119 227C69 232 29 224 5 227C-6 158 3 73 0 4Z" fill="#eef6ff" stroke="#5b8def" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><text class="hand" x="27" y="44" fill="{INK}" font-size="27" font-weight="900">anjing-anjing</text><text class="hand" x="29" y="75" fill="#374151" font-size="18" font-weight="800">个人 AI 桌面助手</text><text class="hand" x="29" y="101" fill="#6b7280" font-size="15" font-weight="800">12 条成长赛道的统一入口</text><g transform="translate(95 119) scale(.72)">{platform_icon('#5b8def','#eef6ff')}</g></g>
  <g transform="translate(433 135)"><path d="M0 8C66-4 132 3 197 0C251-3 297 1 332 9C337 62 329 171 335 224C258 234 182 221 118 228C67 233 29 223 5 227C-5 160 4 77 0 8Z" fill="#fff4ee" stroke="#e98263" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><text class="hand" x="27" y="44" fill="{INK}" font-size="27" font-weight="900">anjing-aigc</text><text class="hand" x="29" y="75" fill="#374151" font-size="18" font-weight="800">AIGC 图文创作工作台</text><text class="hand" x="29" y="101" fill="#6b7280" font-size="15" font-weight="800">灵感 → 内容 → 多平台资产</text><g transform="translate(103 116) scale(.72)">{aigc_icon('#e98263','#fff4ee')}</g></g>
  <g transform="translate(800 135)"><path d="M0 4C75-7 135 5 202 0C254-3 302 2 334 8C338 60 329 174 335 224C256 233 182 222 118 228C67 233 29 223 5 227C-6 159 3 73 0 4Z" fill="#f3faef" stroke="#79b36a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><text class="hand" x="27" y="44" fill="{INK}" font-size="27" font-weight="900">anjing-richfree</text><text class="hand" x="29" y="75" fill="#374151" font-size="18" font-weight="800">AI 投资监控工具</text><text class="hand" x="29" y="101" fill="#6b7280" font-size="15" font-weight="800">信息 → 信号 → 决策观察</text><g transform="translate(61 126)"><rect x="0" y="0" width="205" height="76" rx="12" fill="{PAPER}" class="line"/><path d="M20 58c25-9 34-28 53-22 21 7 30-17 49-10 18 7 31-11 61-18" stroke="#79b36a" stroke-width="6" fill="none" stroke-linecap="round" class="draw"/><path d="M170 8h15v15" stroke="#79b36a" stroke-width="5" fill="none"/><circle cx="74" cy="36" r="7" fill="#f3c969" class="pulse"/><circle cx="122" cy="26" r="7" fill="#e98263" class="pulse" style="animation-delay:.4s"/></g></g>
</svg>
"""


def signals_svg() -> str:
    return f"""<svg width="1200" height="250" viewBox="0 0 1200 250" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">GitHub signals</title><desc id="desc">持续构建、发布与分享的公开信号。</desc>
{COMMON_STYLE}
  <rect width="1200" height="250" rx="28" fill="{PAPER}"/>
  <path d="M34 28C191 17 323 35 474 25C635 15 823 25 1163 31C1171 87 1158 173 1164 220C941 235 741 219 574 229C382 239 188 218 37 225C25 157 37 91 34 28Z" fill="#fffaf0" stroke="{INK}" stroke-opacity=".72" stroke-width="5"/>
  <text class="hand" x="68" y="77" fill="{INK}" font-size="37" font-weight="900">Open work leaves signals</text><text class="hand" x="70" y="109" fill="#5b6472" font-size="20" font-weight="800">持续构建，比一次性的“完成”更重要</text>
  <path d="M487 122h565" stroke="#9ca3af" stroke-width="4" stroke-dasharray="8 11" class="flow"/>
  <g transform="translate(468 91)"><rect width="164" height="89" rx="18" fill="#eef6ff" stroke="#5b8def" stroke-width="5"/><text class="hand" x="30" y="39" fill="{INK}" font-size="22" font-weight="900">BUILD</text><path d="M31 61h101" stroke="#5b8def" stroke-width="5" stroke-linecap="round"/><circle cx="53" cy="61" r="8" fill="#5b8def" class="pulse"/></g>
  <g transform="translate(684 91)"><rect width="164" height="89" rx="18" fill="#fff4ee" stroke="#e98263" stroke-width="5"/><text class="hand" x="39" y="39" fill="{INK}" font-size="22" font-weight="900">SHIP</text><path d="M33 64l45-28 53 28" stroke="#e98263" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="78" cy="37" r="8" fill="#f3c969" class="bob"/></g>
  <g transform="translate(900 91)"><rect width="164" height="89" rx="18" fill="#f3faef" stroke="#79b36a" stroke-width="5"/><text class="hand" x="32" y="39" fill="{INK}" font-size="22" font-weight="900">SHARE</text><path d="M43 68l37-29 40 29" stroke="#79b36a" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="43" cy="68" r="7" fill="#79b36a" class="pulse"/><circle cx="80" cy="39" r="7" fill="#f3c969" class="pulse" style="animation-delay:.3s"/><circle cx="120" cy="68" r="7" fill="#e98263" class="pulse" style="animation-delay:.6s"/></g>
</svg>
"""


def main() -> None:
    def clean(svg: str) -> str:
        return "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"

    CARDS.mkdir(parents=True, exist_ok=True)
    for data in CARD_DATA:
        slug = data[0]
        (CARDS / f"{slug}.svg").write_text(clean(card_svg(*data)), encoding="utf-8")
    (ANIMATED / "open-source-route.svg").write_text(clean(route_svg()), encoding="utf-8")
    (ANIMATED / "products-showcase.svg").write_text(clean(products_svg()), encoding="utf-8")
    (ANIMATED / "github-signals.svg").write_text(clean(signals_svg()), encoding="utf-8")
    print(f"Generated {len(CARD_DATA) + 3} SVG assets")


if __name__ == "__main__":
    main()
