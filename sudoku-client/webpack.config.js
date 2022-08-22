const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: './js/index.ts',
    output: {
        path: path.resolve(__dirname, 'build'),
        filename: 'bundle.js',
        library: 'App',
    },
    plugins: [
        new CleanWebpackPlugin(),
        new MiniCssExtractPlugin(),
        new HtmlWebpackPlugin({
            title: 'Sudoku',
            filename: 'index.html',
            template: './html/index.html',
        }),
    ],
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: "ts-loader",
                exclude: path.resolve(__dirname, 'node_modules'),
            },
            {
                test: /\.js$/,
                exclude: path.resolve(__dirname, 'node_modules'),
            },
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                ],
                exclude: path.resolve(__dirname, 'node_modules'),
            },
        ]
    },
    resolve: {
        extensions: ['.ts', '.js'],
    },
    mode: 'development',
    devtool: 'source-map',
    devServer: {
        watchFiles: ['html/index.html'],
        compress: true,
        port: 9000,
    },
}
