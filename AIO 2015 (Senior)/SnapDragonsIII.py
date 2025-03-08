# https://orac2.info/problem/274/
N = int(input())
 
answer = 0
 
p_first_found_list = [False for i in range(N + 1)]
p_last_found_list = [False for i in range(N + 1)]
p_first_pos_list = [None for i in range(N + 1)]
 
last_card = None
card_in_search = None
card_in_search_pos = 0
 
for i in range(2 * N):
    card = int(input())
    
    if not p_first_found_list[card]:
        p_first_found_list[card] = True
        p_first_pos_list[card] = i
    elif not p_last_found_list[card]:
        p_last_found_list[card] = True
        
    if (card_in_search is None):
        if not p_last_found_list[card]:
            card_in_search = card
            card_in_search_pos = i
    elif card == card_in_search:
        answer += 1
        if p_last_found_list[last_card]:
            card_in_search = None
        else:
            card_in_search = last_card
            card_in_search_pos = i
    else:
        if card == last_card:
            answer += 1
        elif (
            p_last_found_list[card] 
            and p_first_pos_list[card] > card_in_search_pos 
        ):
            answer += 1
            if p_last_found_list[last_card]:
                card_in_search = None
            else:
                card_in_search = last_card
                card_in_search_pos = i
    
    last_card = card

# freaky problem

print(answer)