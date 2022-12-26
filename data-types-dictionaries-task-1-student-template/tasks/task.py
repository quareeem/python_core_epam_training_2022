from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    dic = {}
    for item in s.lower():
        dic[item] = dic.get(item, 0) + 1

    return dic
