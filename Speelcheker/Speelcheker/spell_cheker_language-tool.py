import language_tool_python

# language_tool = language_tool_python.LanguageTool('en-US', config={'maxSpellingSuggestions': 1})

# tool = language_tool_python.LanguageTool('en-US')  # use a local server (automatically set up), language English
# # tool = language_tool_python.LanguageTool('ru-RU')
# text = 'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
# matches = tool.check(text)
# print(matches)
# print(len(matches))
#
# print(matches[0].ruleId, matches[0].replacements)
# print(matches[1].ruleId, matches[1].replacements)
# print(matches[1])


tool = language_tool_python.LanguageTool('ru-RU')
text = 'Длина реки, длина волос.'
# text = 'Длинная длинна. Проверкка текста на ашибки.'
matches = tool.check(text)

print(len(matches), matches)
for m in matches:
    print(m.ruleIssueType, m.replacements)




tool.close()




