import re, sys, html, os
def convert(path):
    s = open(path, encoding='utf-8', errors='replace').read()
    s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', s, flags=re.S)
    # replace math by alttext
    def rep(m):
        alt = re.search(r'alttext="([^"]*)"', m.group(0))
        return ' $' + html.unescape(alt.group(1)) + '$ ' if alt else ' '
    s = re.sub(r'<math\b.*?</math>', rep, s, flags=re.S)
    # keep section headings visible
    s = re.sub(r'<h([1-6])[^>]*>(.*?)</h\1>', lambda m: '\n\n## ' + re.sub(r'<[^>]+>', '', m.group(2)) + '\n', s, flags=re.S)
    s = re.sub(r'</p>|<br\s*/?>|</div>|</li>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n\n', s)
    return s.strip()
for p in sys.argv[1:]:
    t = convert(p)
    out = p[:-5] + '.txt'
    open(out, 'w', encoding='utf-8').write(t)
    print(out, len(t), 'chars')
