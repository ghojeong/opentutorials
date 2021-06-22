const path = require("path");

module.exports = {
    mode: "production",
    entry: {
        index: "./src/entry/index.js",
        about: "./src/entry/about.js"
    },
    output: {
        path: path.resolve(__dirname, "./src/dist"),
        filename: "[name]_bundle.js",
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    "style-loader",
                    "css-loader"
                ]
            }
        ]
    }
}
