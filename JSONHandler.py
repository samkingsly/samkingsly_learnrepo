import json

with open('D:\GitHub\samkingsly_learnrepo\ex5.json', 'r') as file:
    ex5 = json.load(file)

    for i in ex5:
        if i['name'] == 'Old Fashioned' and i['type'] == 'donut':
            x = i['batters']['batter']

            for id in x:
                cur_id = id["id"]
                last_id = cur_id
            last_id=int(last_id) + 1
            z={ "id": last_id, "type": "Coffee" }
            x.append(z)
    print(ex5)
        
with open('D:\GitHub\samkingsly_learnrepo\ex5.json','w') as out:
    json.dump(ex5,out,indent=4)



