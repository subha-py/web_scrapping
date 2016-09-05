from twitter import Twitter,OAuth
import pprint
t=Twitter(auth=OAuth('176509270-mHTe3L9yT3ggR78vXOViatQfctchLfRVrFZzqBwu',
                     'xieJy3Yn6D05ZhohvzrRBGYBPoM8J94OhsHgmBUd03Vyq',
                     'HmtEdYUbFwLZEyvTC7UkG0UwJ',
                     'zWLh6kVKQNY72eOhPjpUI3hreDsOXNd4TI1Y9J6gyoHP4UycAx'))
# statusUpdate = t.statuses.update(status='Hello, world2!')
# print(statusUpdate)
pp=pprint.PrettyPrinter(indent=4)
pythonStatuses=t.statuses.user_timeline(screen_name='didhitimimi',count=5)
pp.pprint(pythonStatuses)