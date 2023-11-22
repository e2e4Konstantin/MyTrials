#
# pip install --upgrade language_tool_python
# java -version
#
# spellchecker for OpenOffice
#
import language_tool_python

# use a local server automatically set up
# tool = language_tool_python.LanguageTool('ru-RU')

# remote server use the public API
tool = language_tool_python.LanguageToolPublicAPI('ru')


# language_tool = language_tool_python.LanguageTool('en-US', config={'maxSpellingSuggestions': 5})
# # tool = language_tool_python.LanguageTool('ru-RU')
# text = 'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
# matches = tool.check(text)
# print(matches)
# print(len(matches))
#
# print(matches[0].ruleId, matches[0].replacements)
# print(matches[1].ruleId, matches[1].replacements)
# print(matches[1])


#text = 'Длина реки, длина волос.'
text = 'Кислое Малако. Длинная длинна. Река длиНа и широка. ПрАверка текста на ашибки.'
matches = tool.check(text)

print(len(matches), matches)
for m in matches:
    print(m.ruleIssueType, m.replacements)




tool.close()




