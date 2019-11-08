import torch
import torchvision

import praw

with open("client.secret") as secret:
    sec_str = secret.read().strip()
    print(sec_str)
    reddit = praw.Reddit(user_agent='persuasion_embedder',
                        client_id='7-RsL44iU7tDdg', client_secret=sec_str)
    

subreddit = reddit.subreddit('changemyview')
submissions = [submission for submission in subreddit.top(time_filter='month',limit=1000)]

[submission.comments.replace_more(limit=None) for submission in submissions]

delta_awarded_id = list(map(lambda x: praw.models.Comment(reddit, id=x[0]).parent(), list(filter(lambda x: ('Confirmed: 1 delta awarded to' in x[1] and x[2] == "deltabot"), [(comment.id, comment.body, comment.author) for submission in submissions for comment in submission.comments.list()]))))

delta_awarded_text = list(map(lambda x: x.parent().body,delta_awarded_id))

[print('+++++++\n\n', text, '\n') for text in delta_awarded_text]


       