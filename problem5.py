class User:
    def __init__(self, name):
        self.name = name

    # To print a human readable object name
    def __repr__(self):
        return '{}'.format(self.name)


def find_transaction(user_input):
    transactions = {}
    formatted_transaction = []
    for item in user_input:
        for sharer in item['share_by']:
            if item['user'] != sharer:
                if (item['user'], sharer) in transactions.keys():
                    transactions[(item['user'], sharer)] += float(item['amount'] / len(item['share_by']))
                elif (sharer, item['user']) in transactions.keys():
                    transactions[(sharer, item['user'])] -= float(item['amount'] / len(item['share_by']))
                else:
                    transactions[(item['user'], sharer)] = float(item['amount'] / len(item['share_by']))
    for k, v in transactions.items():
        if v < 0:
            print("{} will pay {} taka to {}".format(k[0], abs(v), k[1]))
            formatted_transaction.append({'from': k[0], 'to': k[1], 'amount': abs(v)})
        else:
            print("{} will pay {} taka to {}".format(k[1], v, k[0]))
            formatted_transaction.append({'from': k[1], 'to': k[0], 'amount': v})
    print(formatted_transaction)
    return formatted_transaction


if __name__ == '__main__':
    print('Running a sample transaction :: for demonstration purpose only')
    user_1 = User('user_1')
    user_2 = User('user_2')
    user_3 = User('user_3')

    inputs = [
        {'user': user_1, 'amount': 50, 'share_by': [user_1, user_2, user_3]},
        {'user': user_2, 'amount': 100, 'share_by': [user_1, user_3]},
    ]

    find_transaction(inputs)
