class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_of_ints = ""
        for i in digits:
            string_of_ints += str(i)
            
        unknown_int = int(string_of_ints) + 1
        
        new_list_of_ints = []
        
        for i in str(unknown_int):
            new_list_of_ints.append(int(i))
            
        return new_list_of_ints
