spice_mix=set()

print(spice_mix)
print(f"intial Id: {id(spice_mix)}")
spice_mix.add("cardamom")
spice_mix.add("red chilli")
spice_mix.add("salt")

print(spice_mix)
print(f"after change Id: {id(spice_mix)}")

#### Output
# set()
# intial Id: 2103475765984             we can see even if we want to change the value in side the set it doestnt change it refaracne id 
# {'red chilli', 'salt', 'cardamom'}
# after change Id: 2103475765984