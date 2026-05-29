import os
import glob

# Update Python scripts in data_update
data_update_scripts = glob.glob(r'd:\ag_coding_ex\jphanja\scripts\data_update\*.py')
for script in data_update_scripts:
    with open(script, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # kanji_gradeX.json -> ../../data/kanji/kanji_gradeX.json
    content = content.replace('"kanji_grade', '"../../data/kanji/kanji_grade')
    content = content.replace("'kanji_grade", "'../../data/kanji/kanji_grade")
    
    # radical/src/data/ -> ../../radical/src/data/
    content = content.replace("'radical/src/data/", "'../../radical/src/data/")
    content = content.replace('"radical/src/data/', '"../../radical/src/data/')
    
    with open(script, 'w', encoding='utf-8') as f:
        f.write(content)

# Update Python scripts in audio
audio_scripts = glob.glob(r'd:\ag_coding_ex\jphanja\scripts\audio\*.py')
for script in audio_scripts:
    with open(script, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('"nabiwapull.JSON"', '"../../data/stories/nabiwapull.JSON"')
    content = content.replace('"dendenmushikanashi.JSON"', '"../../data/stories/dendenmushikanashi.JSON"')
    content = content.replace('"kaninotokoya.JSON"', '"../../data/stories/kaninotokoya.JSON"')
    
    with open(script, 'w', encoding='utf-8') as f:
        f.write(content)

# Update index.html
html_file = r'd:\ag_coding_ex\jphanja\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace JS fetch paths in index.html
html_content = html_content.replace("'kaninotokoya.JSON'", "'data/stories/kaninotokoya.JSON'")
html_content = html_content.replace("'nabiwapull.JSON'", "'data/stories/nabiwapull.JSON'")
html_content = html_content.replace("'dendenmushikanashi.JSON'", "'data/stories/dendenmushikanashi.JSON'")
html_content = html_content.replace("'convenience_scenesv1.JSON'", "'data/scenes/convenience_scenesv1.JSON'")
html_content = html_content.replace("'shopping_scenesv1.JSON'", "'data/scenes/shopping_scenesv1.JSON'")
html_content = html_content.replace("'airport_scenesv1.JSON'", "'data/scenes/airport_scenesv1.JSON'")
html_content = html_content.replace("'izakaya_scenesv1.JSON'", "'data/scenes/izakaya_scenesv1.JSON'")
html_content = html_content.replace("`kanji_grade${grade}.json`", "`data/kanji/kanji_grade${grade}.json`")

# Update temp.js reference if any
html_content = html_content.replace('temp.js', 'app.js')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Replacement complete.')
