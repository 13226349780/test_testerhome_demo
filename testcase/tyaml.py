import yaml


stream = open('../ymal/url.ymal')
data = yaml.load(stream)
print(data['url'])
