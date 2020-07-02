# Given a string, find the length of the longest substring without repeating characters.

"""
check if string provided is empty.If true return 0

window var is a string with unique characters this window slides thru s

left is the left most character on the window str

cur_len is the current length of the window at that time

max_len is the maximum length achieved by the window so far


steps::

1. loop through the string s

2. if the current character 'ch' which is supposed to be entering the 'window'
   is currently in window delete the 'left' most character until the character same to
   'ch' is deleted ( achieved using a while loop)

3. when deleting the 'left' variable which is the index of left most char increases by one
   hence the 'adding of left +=1'
   when deleting the current len of the window reduces by one hence the 'cur_len -=1'

4. While loop breakes when ch is no longer in 'window'

5. Add the new 'ch' in window

6. Update the current len of window to +=1

7. Update the max_len to the bigest val between current max_len and current cur_len of windows

8. Return the max_len

"""
def lengthOfLongestSubstring(s):

        if len(s)== 0:
            return  0

        window = set()

        left =0

        cur_len =0

        max_len =0

        for ch in s:
            while ch in window:
                window.remove(s[left])

                left+=1
                cur_len -=1
            window.add(ch)
            cur_len+=1

            max_len = max(max_len, cur_len)

        print(max_len)




s= "ABBA"
lengthOfLongestSubstring(s)

