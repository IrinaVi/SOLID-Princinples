# In the open/closed principle classes should be open for extension, but closed for modification.
# Essentially meaning that classes should be extended to change functionality, rather than being altered into something else.

#  In doing so, we stop ourselves from modifying existing code and causing potential new bugs in an otherwise happy application.
# Of course, the one exception to the rule is when fixing bugs in existing code.

# When business requirements change and we need to add or alter the existing functionality
# New methods and behaviours can be extended to it, but it cannot be modified.

# Other classes depend on the existing functionality and I change it, I may introduce bugs somewhere where I don't even know.

