#!/usr/bin/env python3
"""每日刷新 GitHub profile README 中的数字（stars / 已合并 PR / npm 下载数）。
锚点正则只替换数字、不动结构；数据缺失或锚点未命中则保留原值并告警。"""
import os, re, sys, urllib.request

TOKEN = os.environ.get('GITHUB_TOKEN', '')
GH = {'Authorization': f'Bearer {TOKEN}'} if TOKEN else {}

def get(url, headers=None, timeout=15):
    h = dict(headers or {})
    if 'api.github.com' in url and GH:
        h.update(GH)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode('utf-8', 'replace')

def jget(url):
    import json
    return json.loads(get(url))

def gh_stars(repo):
    return jget(f'https://api.github.com/repos/{repo}').get('stargazers_count')

def gh_merged(repo):
    d = jget(f'https://api.github.com/search/issues?q=author:AdamPlatin123+repo:{repo}+type:pr+is:merged&per_page=1')
    return d.get('total_count')

def safe(name, fn):
    try:
        return fn()
    except Exception as e:
        print(f'[warn] {name}: {e}', file=sys.stderr)
        return None

R = {
    'radar_s': safe('radar-stars', lambda: gh_stars('AdamPlatin123/dsh-plugin-radar')),
    'tui_s': safe('tui-stars', lambda: gh_stars('ccch1mneyyy/dsh-TUI')),
    'tui_p': safe('tui-prs', lambda: gh_merged('ccch1mneyyy/dsh-TUI')),
    'odr_s': safe('odr-stars', lambda: gh_stars('AdamPlatin123/Open-Deep-Research-workflow-on-Dify')),
    'adw_s': safe('adw-stars', lambda: gh_stars('svcvit/Awesome-Dify-Workflow')),
    'al_s': safe('anywhere-stars', lambda: gh_stars('anywhere-labs/dsh-desktop')),
    'al_p': safe('anywhere-prs', lambda: gh_merged('anywhere-labs/dsh-desktop')),
    'zcf_d': safe('zcf-downloads', lambda: jget('https://api.npmjs.org/downloads/point/last-year/dsh-zcf')['downloads']),
}

comma = lambda n: f'{n:,}'
k1 = lambda n: f'{n/1000:.1f}'          # 10,782 → 10.8（配合锚点里的 k）
k_plus = lambda n: f'{n:,}+'            # 8,500+ 形式

# (名称, 正则, 值键, 数字格式) —— 两个捕获组夹住数字，替换为 组1+格式化值+组2
RULES = [
    ('radar★·标题', r'(### \[dsh-plugin-radar\]\([^)]*\) · ★)[\d,]+( · Owner)', 'radar_s', comma),
    ('TUI★·标题', r'(### \[dsh-TUI\]\([^)]*\) · ★)[\d,]+( · Admin)', 'tui_s', comma),
    ('ODR★·标题', r'(### \[Open-Deep-Research-workflow-on-Dify\]\([^)]*\) · ★)[\d,]+( · Owner)', 'odr_s', comma),
    ('TUI·merged正文', r'(\*\*)\d+( merged PRs\*\* spanning)', 'tui_p', str),
    ('TUI·merged链接', r'(→ \[All )\d+( merged dsh-TUI PRs\])', 'tui_p', str),
    ('Awesome★', r'(\[Awesome-Dify-Workflow \()[\d.]+(k★\)\]\()', 'adw_s', k1),
    ('anywhere-labs★', r'(anywhere-labs, )[\d.]+(k★\))', 'al_s', k1),
    ('anywhere-labs·PR', r'(anywhere-labs, [\d.]+k★\) \| \*\*)\d+( merged PRs)', 'al_p', str),
    ('zcf下载·正文', r'(npm — )[\d,]+\+?( cumulative downloads)', 'zcf_d', k_plus),
    ('zcf下载·时间线', r'(dsh-zcf \()[\d,]+\+?( downloads\))', 'zcf_d', k_plus),
    ('ODR★·时间线', r'(Open-Deep-Research-workflow-on-Dify \()[\d,]+(★\))', 'odr_s', comma),
    ('radar★·时间线', r'(dsh-plugin-radar \()[\d,]+(★\))', 'radar_s', comma),
]

def apply_rules(s):
    for name, pat, key, fmt in RULES:
        val = R[key]
        def repl(m, val=val, fmt=fmt, name=name):
            if val is None:
                print(f'[warn] {name} 数据缺失，保留原值', file=sys.stderr)
                return m.group(0)
            return m.group(1) + fmt(val) + m.group(2)
        s, n = re.subn(pat, repl, s)
        if n == 0:
            print(f'[warn] 锚点未命中——{name}', file=sys.stderr)
    # TUI 时间线（★数与 merged 各自独立判断，缺一项只改另一项）
    if R['tui_s'] is not None:
        s, n = re.subn(r'(dsh-TUI \()[\d,]+(★,)', lambda m: f'{m.group(1)}{comma(R["tui_s"])}{m.group(2)}', s)
        if n == 0:
            print('[warn] 锚点未命中——TUI时间线★', file=sys.stderr)
    if R['tui_p'] is not None:
        s, n = re.subn(r'(★, )\d+( merged)', lambda m: f'{m.group(1)}{R["tui_p"]}{m.group(2)}', s)
        if n == 0:
            print('[warn] 锚点未命中——TUI时间线merged', file=sys.stderr)
    return s

src = open('README.md', encoding='utf-8').read()
s = apply_rules(src)
if s != src:
    open('README.md', 'w', encoding='utf-8').write(s)
    print('[ok] README.md 已更新')
else:
    print('[ok] README.md 无变化')
