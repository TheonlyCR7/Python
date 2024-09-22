def hello(greeting = 'Hello', name = 'world'):
	print('{}, {}!'.format(greeting, name))
params = {'name': 'bobo', 'greeting': 'well met'}
hello()
hello(**params)