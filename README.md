# github-markdown
This repo provides a [Pandoc filter](https://pandoc.org/filters.html) to help convert LaTeX math to Github-flavored markdown.
In particular, the focus is on using the correct delimiters ``$`...`$`` and `` ```math...``` `` for inline and display math, respectively.

It uses the `pandocfilters` package, installable via
```
pip install pandocfilters
```

## Usage
Example usage might be
```
pandoc -s mathy_doc.tex -o doc.md --filter github_md.py
```
