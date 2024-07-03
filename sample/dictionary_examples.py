sample_dictionary = {"Prakasha":9916495865, "nithin":999}
# print (sample_dictionary)
# print(sample_dictionary.keys())
# print(sample_dictionary.values())


for names in sample_dictionary.keys():
    if names == "Prakasha":
        print(f"found the contact {names} {sample_dictionary[names]}")


sample_dictionary["Madhan"] = 888


second_dict = {"jaya":"77", "sample_dictionary":sample_dictionary}
print(second_dict)

print(second_dict['sample_dictionary'])
