const arrowKeys = [ "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight" ];
const digitKeys = [ ...Array(9).keys() ].map(index => (index + 1).toString());

export function isArrowKey(key){
    return arrowKeys.includes(key);
}

export function isDigitKey(key){
    return digitKeys.includes(key);
}