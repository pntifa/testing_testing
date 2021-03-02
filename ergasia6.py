import tweepy
import tkinter
from itertools import count

str=' '
#Add your Tokens
auth = tweepy.OAuthHandler('XXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
auth.set_access_token('XXXXXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

userID = input('Give Profile:')
user = api.get_user(userID)

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

for info in tweets[:10]:
    print("ID: {}".format(info.id))
    print(info.created_at)
    print(info.full_text)
    str+=info.full_text
    print("\n")

#Convert string to list
def Convert(string): 
    li = list(string.split(' ')) 
    return li 

#find 5 longest words
def longest_word(lst, K): 
    cnt = count() 
    return sorted(lst, key = lambda w : (len(w), next(cnt)), reverse = True)[:K] 

#find 5 shortest words
def shortest_word(lst, K): 
    cnt = count() 
    return sorted(lst, key = lambda w : (len(w), next(cnt)), reverse = False)[:K]

# Driver code 
lst = Convert(str)
K = 5
print('The 5 Longest words:' , '\n')
print(longest_word(lst, K))
print('\n')
print('The 5 Shortest words:' , '\n')
print(shortest_word(lst, K))
