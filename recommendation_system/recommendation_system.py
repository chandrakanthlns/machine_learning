import pandas as pd
import json
import numpy as np
# import our cosine_similarity function from sklearn
from sklearn.metrics.pairwise import cosine_similarity


data = pd.read_csv("clean_data.csv")
result = pd.DataFrame({"Id":data['id'],
                       "Username" : data['reviews_username'],
                     "Product":data['name'],
                     "Rating": data['reviews_rating']})

result1 = result.pivot_table(index="Id",columns=["Product","Username"],values="Rating").fillna(0)

allreviewids = result1.values
reviews = allreviewids[0]
denom = np.sqrt(sum(np.square(x) for x in reviews))
cosinesimiilarity = [("AV1YIch7GV-KLJ3addeG",1)]
i = 1
for review in allreviewids[1:]:
    numerator = [x*y for x,y in zip(reviews,review)]
    denom2 = np.sqrt(sum(np.square(x) for x in review))
    costheta = sum(numerator) / (denom * denom2)
    
    cosinesimiilarity.append((result1.index[i],costheta))
    i +=1
cosinesimiilarity.sort(key=lambda x: x[1],reverse=True)

sim20users = cosinesimiilarity[0:20]
user_user_sim_matrix = pd.DataFrame(cosine_similarity(result1))
user_user_sim_matrix.columns = result1.index
user_user_sim_matrix['Id'] = result1.index
user_user_sim_matrix = user_user_sim_matrix.set_index('Id')

def review_id(username,reviewid):
    items_bought = set(result1.loc[reviewid].iloc[result1.loc[reviewid].to_numpy().nonzero()].index)
    for each_user in items_bought:
        item = each_user[0]
    return item
    

def get_items_to_recommend_cust(username,cust_a="AVpfPjqKLJeJML435aZR"):
    '''returns the items to recommend to a customer using customer similarity'''
    # _most_similar_user = user_user_sim_matrix.loc[cust_a].sort_values(ascending=False).reset_index().iloc[1:,0][:5].tolist()
    items_brought = review_id(username,cust_a)
    return items_brought


# print(get_items_to_recommend_cust("debbie"))

if __name__ == "__main__":
    username = "debbie"
    cust_a="AVpfPjqKLJeJML435aZR"
    get_items_to_recommend_cust(username,cust_a)    