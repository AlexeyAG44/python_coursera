# Есть две коробки,
# первая размером A₁×B₁×C₁,
# вторая размером A₂×B₂×C₂.
# Определите, можно ли разместить одну из этих коробок внутри другой,
# при условии, что поворачивать коробки можно только на 90 градусов вокруг ребер.

a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
p1 = (a1 == a2 and b1 == b2 and c1 == c2)
p2 = (a1 == a2 and b1 == c2 and c1 == b2)
p3 = (a1 == c2 and b1 == a2 and c1 == b2)
p4 = (a1 == b2 and b1 == a2 and c1 == c2)
p5 = (a1 == b2 and b1 == c2 and c1 == a2)
p6 = (a1 == c2 and b1 == b2 and c1 == a2)
p11 = (a1 <= a2 and b1 <= b2 and c1 <= c2)
p21 = (a1 <= a2 and b1 <= c2 and c1 <= b2)
p31 = (a1 <= c2 and b1 <= a2 and c1 <= b2)
p41 = (a1 <= b2 and b1 <= a2 and c1 <= c2)
p51 = (a1 <= b2 and b1 <= c2 and c1 <= a2)
p61 = (a1 <= c2 and b1 <= b2 and c1 <= a2)
p111 = (a1 >= a2 and b1 >= b2 and c1 >= c2)
p211 = (a1 >= a2 and b1 >= c2 and c1 >= b2)
p311 = (a1 >= c2 and b1 >= a2 and c1 >= b2)
p411 = (a1 >= b2 and b1 >= a2 and c1 >= c2)
p511 = (a1 >= b2 and b1 >= c2 and c1 >= a2)
p611 = (a1 >= c2 and b1 >= b2 and c1 >= a2)
if p1 or p2 or p3 or p4 or p5 or p6:
    print("Boxes are equal")
elif p11 or p21 or p31 or p41 or p51 or p61:
    print("The first box is smaller than the second one")
elif p111 or p211 or p311 or p411 or p511 or p611:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
