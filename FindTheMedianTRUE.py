# this input list contains duplicates
mylist = [5, 3, 5, 2, 1, 6, 6, 4] # 5 & 6 are duplicate numbers.
# find the length of the list
print(len(mylist), mylist)
# create a set from the list
myset = set(mylist)
# find the length of the Python set variable myset
print(len(myset), myset)
# compare the length and print if the list contains duplicates
if len(mylist) != len(myset):
    print("duplicates found in the list")
else:
    print("No duplicates found in the list")
    