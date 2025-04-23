names=set()
names.update(["prapti","manya","shreya","vandita","kosha"])
print(names)

if "prapti" in names:
    names.remove("prapti")
    names.add("prapti patel")

    print(names)
    names.discard("prapti patel")
    names.discard("manya")

    print(names)