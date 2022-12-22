class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_dict = {}
        replaced_chars = set()

        s_len = len(s)
        if s_len != len(t):
            return False

        for i in range(s_len):
            s_char = s[i]
            t_char = t[i]
            try:
                mapped_t_char = map_dict[s_char]
                if mapped_t_char != t_char:
                    return False
            except KeyError:
                if t_char in replaced_chars:
                    return False # char has already been exchanged for another one
                map_dict[s_char] = t_char
                replaced_chars.add(t_char)

        
        return True
