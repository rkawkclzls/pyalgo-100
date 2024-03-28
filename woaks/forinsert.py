# Double linked list

node1 = {
    'pre': None,
    'data': 12,
    'next': None
}

node2 = {
    'pre': None,
    'data': 99,
    'next': None
}

node3 = {
    'pre': None,
    'data': 37,
    'next': None
}

node1['next'] = node2
node2['pre'] = node1

node2['next'] = node3
node3['pre'] = node2

print(node1['next']['next']['pre']['next']['pre']['pre']['data'])

node1 = {
    'data': 12,
    'children': []
}

node2 = {
    'data': 99,
    'children': []
}

node3 = {
    'data': 37,
    'children': []
}

node1['children'].append(node2)
node1['children'].append(node3)

print(node1['children'][0]['data'])  # prints 99
print(node1['children'][1]['data'])  # prints 37