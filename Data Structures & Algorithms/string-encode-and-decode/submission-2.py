class Solution:
    length_delimiter = "#"
    string_delimiter = '|'

    def encode(self, strs: List[str]) -> str:
        lengths = list()

        for item in strs:
            lengths.append(str(len(item)))
        
        lengths_metadata = self.length_delimiter.join(lengths)

        return lengths_metadata + self.string_delimiter + "".join(strs)

    def decode(self, s: str) -> List[str]:
        lengths_metadata = s.split(self.string_delimiter)[0]

        if not lengths_metadata:
            return []
            
        lengths = [int(x) for x in lengths_metadata.split(self.length_delimiter)]

        output = list()
        pointer = len(lengths_metadata) + 1

        for length in lengths:
            output.append(s[pointer:pointer + length])
            pointer += length
        
        return output
