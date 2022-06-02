const express = require("express")
const cors = require("cors")

const api = express()
api.use(cors)

api.post("/", (req, res) => {
    res.send("Hello World!")
})


api.listen(3001, () => {
    console.log("running");
})


