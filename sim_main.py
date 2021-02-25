"""
similarity_measure 함수 Use Example

input:

- keyword_A = "코로나"
- index_A = [0,1,2,3,4,5,6,7,8,9]
- keyword_B = "바이오"
- index_B = [0,1,2,3,4,5,6,7,8,9]

output:

A_list, B_list, AB_list, A_avg, B_avg, AB_avg

"""

from similarity_measure import similarity_measure

keyword_A = "코로나"
index_A = [0, 1, 3]  # 유저가 선택한 코로나 기사들 index
keyword_B = "바이오"
index_B = [0, 1, 2, 3]  # 유저가 선택한 바이오 기사들 index

A_list, B_list, AB_list, A_avg, B_avg, AB_avg = similarity_measure(keyword_A, index_A, keyword_B, index_B)

print("A_avg : ", A_avg)
print("B_avg : ", B_avg)
print("AB_avg : ", AB_avg)

print("A_list : ", A_list)
print("B_list : ", B_list)
print("AB_list : ", AB_list)

