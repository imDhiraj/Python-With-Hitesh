chai_type ="ginger Tea"
chai_for = "Dhiraj"

print (f"chai for {chai_for}:{chai_type}")

# -- Indexing--
#string are inclusive which means include the boundreies like if we have word with 10 charaters in it even if it asart counting from 0 while printing it we need to put total number of charaters

chai_with_description="aramatical wa chai"
#                aramatical has 10 words
print(f"the chai feels like {chai_with_description[0:9]}")
# the chai feels like aramatica

print(f"the chai feels like {chai_with_description[0:10]}")
# the chai feels like aramatical

# -- slicing --
# we can set limit as per outr need while performing oprations on the string 
print(f"the chai feels like {chai_with_description[10:]}") # starting from specfic char
print(f"the chai feels like {chai_with_description[:15]}") #or end it at something

print(f"the chai feels like {chai_with_description[0:10:2]}") # we can set intervals while printing the chars as while after the 3rd :: <-this gives interverls

print(f"the chai feels like in reverse  {chai_with_description[::-1]}") # and one of the most simple way of revreseing the string as weile

# -- encode-decode function--
specical_chai = " specicál chai with extra money"
encoded_item = specical_chai.encode("utf-8")
decoded_item = encoded_item.decode("utf-8")
print(f"can we see different charehter come into play wih stirng while send those setences on server {specical_chai}")
print (f"that why a {encoded_item}" )
print(f"so that nothing get loss behind {decoded_item}")

# like this we can use multiple built-in functions we can use 

#Ouputs
# chai for Dhiraj:ginger Tea
# the chai feels like aramatica
# the chai feels like aramatical
# the chai feels like  wa chai
# the chai feels like aramatical wa c
# the chai feels like aaaia
# the chai feels like in reverse  iahc aw lacitamara
# can we see different charehter come into play wih stirng while send those setences on server  specicál chai with extra money
# that why a b' specic\xc3\xa1l chai with extra money'
# so that nothing get loss behind  specicál chai with extra money

