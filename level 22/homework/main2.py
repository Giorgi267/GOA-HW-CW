# გააკეთეთ სია სადაც იქნება 10 ინტეჯერი , ინტეჯერები რომელიბ იქნება 10 ზე ნაკლები append ის დახმარებით შეიყვანეთ ახალ ცხრილში

intigers = [12,2,343,43,123,1,3,8,56,9,10,20,5]
new_nums = []

for i in intigers:
    if i < 10:
        new_nums.append(i)
print(new_nums)