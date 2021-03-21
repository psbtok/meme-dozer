posts = [
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    },
    {
        'author': 'mike hawk',
        'content': 'hello there'
    }
]

context = []
for six_pack in range(len(posts)//6):
    context.append([])
    for i in range(6):
        context[six_pack].append(posts.pop())

for element in context:
    print(element)
