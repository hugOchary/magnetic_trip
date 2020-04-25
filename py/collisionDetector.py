import physicObject

def rectangleCollisionDetector(pObject1, pObject2):
    absDist = abs(pObject1.getAbs() - pObject2.getOrd)
    ordDist = abs(pObject1.getOrd() - pObject2.getOrd())

    minAbsDist = pObject1.getHalfWidth() + pObject2.getHalfWidth
    minOrdDist = pObject1.getHalfHeight() + pObject2.getHalfHeight

    return absDist >= minAbsDist and ordDist >= minOrdDist


