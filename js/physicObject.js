class physicObject {
    constructor(height, width, charge, type) {
        this.height = height;
        this.width = width;
        this.charge = charge || 1;
        this.type = type || physicObject.STATIC

        // positional data
        this.abs = 0
        this.ord = 0

        // velocity
        this.vabs = 0
        this.vord = 0

        // acceleration
        this.aabs = 0
        this.aord = 0

    }

    updatePosition(abs, ord) {
        this.abs = abs
        this.ord = ord
    }

    updatePosition(vabs, vord) {
        this.vabs = vabs
        this.vord = vord
    }

    updateAcceleration(aabs, aord) {
        this.aabs = aabs
        this.aord = aord
    }

    updateType(type) {
        this.type = type
    }

    getAbs() {
        return this.abs
    }

    getOrd() {
        return this.ord
    }

    getHalfWidth() {
        return this.width/2
    }

    getHalfHeight() {
        return this.height/2
    }

    getType() {
        return this.type
    }
}

physicObject.STATIC = "static"

physicObject.DYNAMIC = "dynamic"

