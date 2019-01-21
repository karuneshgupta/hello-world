def studentinfo(*args,**kwargs,):
    print(args)
    print(kwargs)
courses=["maths","arts"]
marks={"maths":"30","arts":"40"}

studentinfo(*courses,**marks)
# one * is used for list and ** are used for dictionary args and kwargs concept
