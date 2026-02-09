# Difference between discard() and remove() in sets:
# remove() deletes the specified element from the set.
# If the element is not present, it raises a KeyError.
#
# discard() also deletes the specified element from the set.
# If the element is not present, it does nothing and does not raise any error.
#
# Hence, discard() is safer when we are not sure whether the element exists in the set,
# while remove() is used when the presence of the element must be ensured.
