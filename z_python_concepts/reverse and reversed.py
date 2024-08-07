st = [1, 2, 3, 4, 5]
st.reverse()
print(st)  # Output: [5, 4, 3, 2, 1]
st = [1, 2, 3, 4, 5]
reversed_st = reversed(st)
print(list(reversed_st))  # Output: [5, 4, 3, 2, 1]
print(st)  # Output: [1, 2, 3, 4, 5] (original list remains unchanged)
'''
Key Differences
Modification:

st.reverse(): Modifies the original list in place.
reversed(st): Does not modify the original list; provides an iterator for a reversed view.
Return Value:

st.reverse(): Returns None.
reversed(st): Returns an iterator.
Usage:

st.reverse(): Used when you want to reverse the original list itself.
reversed(st): Used when you need to iterate over the list in reverse order or need a reversed copy without changing the original list.
'''