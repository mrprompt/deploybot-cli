import json


def body(command, cmd, item):
    if command == "repository" and cmd == "list":
        body = [
            item['id'],
            item['name'],
            item['title'],
        ]
    elif command == "repository" and cmd == "get":
        body = [
            item[7],
            item[0],
            item[2],
        ]
    elif command == "user" and cmd == "list":
        body = [
            item['id'],
            item['first_name'] + ' ' + item['last_name'],
            item['email'],
            item['is_admin'],
        ]
    elif command == "user" and cmd == "get":
        body = [
            item[7],  # id
            item[0] + ' ' + item[1],  # name
            item[4],  # email
            bool(item[5]),  # admin
        ]
    elif command == "environment" and cmd == "list":
        body = [
            item['id'],
            item['repository_id'],
            item['name'],
            item['branch_name'],
            item['is_automatic'],
            item['current_version'],
        ]
    elif command == "environment" and cmd == "get":
        body = [
            item[10],
            item[0],
            item[1],
            item[7],
            item[6],
            item[9],
        ]
    elif command == "deploy" and cmd == "list":
        body = [
            item['id'],
            item['repository_id'],
            item['environment_id'],
            item['state'],
            item['deployed_version'],
        ]
    elif command == "deploy" and cmd == "get":
        body = [
            item[13],
            item[1],
            item[2],
            item[10],
            item[11],
        ]
    elif command == "deploy" and cmd == "trigger":
        body = [
            item[13],
            item[1],
            item[2],
            item[10],
            item[11],
        ]
    elif command == "server" and cmd == "list":
        body = [
            item['id'],
            item['environment_id'],
            item['name'],
            item['protocol'],
        ]
    elif command == "server" and cmd == "get":
        body = [
            item[8],
            item[1],
            item[3],
            item[2],
        ]
    elif command == "help":
        body = [
            item['command'],
            item['description'],
            item['params']
        ]
    else:
        raise IndexError("Body not found")

    return list(map(lambda x: unicode(x), body))


def response(cmd, param, result):
    content = json.loads(result)
    data = []

    if param == 'list':
        items = content.items()

        for item in items[1][1]:
            data.append(body(cmd, param, item))
    else:
        item = content.values()

        data.append(body(cmd, param, item))

    return data