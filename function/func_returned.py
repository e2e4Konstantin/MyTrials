def get_info(text: str):
    return {
        'words': (words := text.split()),
        'word_count': len(words),
        'character_count': len(''.join(words)),
    }

print(get_info('Hello word!'))
