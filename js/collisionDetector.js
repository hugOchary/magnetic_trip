detection(physicObject1, physicObject2) {
    dabs12 = abs(physicObject1.getAbs() - physicObject2.getAbs())
    dord12 = abs(physicObject1.getOrd() - physicObject2.getOrd())

    minAbsDist = physicObject1.getHalfWidth() - physicObject2.getHalfWidth()
    minOrdDist = physicObject1.getHalfHeight() - physicObject2.getHalfHeight()

    if (dabs12 < minAbsDist || dord12 < minOrdDist ) {
        return true
    }

    return false

}