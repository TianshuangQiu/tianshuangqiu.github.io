import mdtex2html

with open("data/rgb_align.md", "r") as f:
    md = f.read()
html = mdtex2html.convert(md)
with open("rgb_align_test.html", "w") as f:
    f.write(html)
print(html)
