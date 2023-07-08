format = 'Hello, %s. %s enough for ya?'
values = ('world', 'Hot')
print(format % values) 

from string import Template

tmp1 = Template("$test")
str1 = tmp1.substitute(test = 'yes')
print(str1)

tmpl = Template("Hello, $who! $what enough for ya?")
str1 = tmpl.substitute(who="Mars", what="Dusty")
print(str1)

str1 = "I am {}. What is your {}?".format("LMC", "name")
print(str1)

str1 = "{1}, {0}, {2}".format("2", "1", "3")
print(str1)

str1 = "{name} {be} {someone}".format(name = "bob", be = "is", someone = "a dog")
print(str1)