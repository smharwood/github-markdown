"""
Pandoc filter to use github/gitlab-style math delimiters in markdown output
"""
import re
from pandocfilters import toJSONFilter, RawInline

def change_delimiters(key, value, fmt, meta):
    """For markdown output, change inline math to github-style delimiters
    for inline: $`...`$
    for display: ```math ... ```
    """
    del meta
    if key == 'Math' and fmt == 'markdown':
        if value[0]['t'] == 'InlineMath':
            return RawInline('markdown', '$`' + value[1] + '`$')
        if value[0]['t'] == 'DisplayMath':
            # also replace '\label' with '\tag' and add an anchor
            content = value[1].strip()
            content = re.sub(r"\\label", r"\\tag", content)
            anchor = '\n'
            m = re.search(r'\\tag{(.*)}', content)
            if m:
                anchor = f'\n<a id="{m.group(1)}"></a>\n'
            return RawInline('markdown', anchor + '```math\n' + content + '\n```\n')
    return

if __name__ == "__main__":
    toJSONFilter(change_delimiters)
