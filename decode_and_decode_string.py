from typing import List

def encode(strs: List[str]) -> str:
    decoded_str = ""
    for s in strs:
        decoded_str = decoded_str + str(len(s)) + "#" + s
    return decoded_str

def decode(string: str) -> List[str]:
    answer = []
    i = 0

    while i < len(string):
        j = i + 1
        while j == "#":
            j += 1

        length = int(string[i:j])
        item = string[j+1:j+length+1]
        answer.append(item)
        i = j+length+1

    return answer


print(decode(encode(["neet","code","love","you"])))
print(decode(encode(["we","say",":","yes"])))
print(decode(encode(["#","##","###","####"])))