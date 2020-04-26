from physicObject import PhysicObject

def computeCollision(obj1, obj2):
    vAbs = obj1.getVAbs()
    vOrd = obj1.getVOrd()

    abs1 = obj1.getAbs()
    abs2 = obj2.getAbs()

    ord1 = obj1.getOrd()
    ord2 = obj2.getOrd()

    alpha = min(
        (abs1-abs2)/vAbs + (obj1.getHalfWidth()+obj2.getHalfWidth())/abs(vAbs),
        (ord1-ord2)/vOrd + (obj1.getHalfHeight()+obj2.getHalfHeight())/abs(vOrd),
    )

    return alpha