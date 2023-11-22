import language_tool_python
tool = language_tool_python.LanguageTool('ru_RU')

text = "Длинна реки, длинна волос. Длинная дорога. Малоко белое."

t = "Зимний мех весьма длиный, и остевые волосы на боках имеют длинну около 50 мм. Малоко белое."

matches = tool.check(t)
print(matches)
for m in matches:
    print(m.ruleIssueType, m.replacements)

