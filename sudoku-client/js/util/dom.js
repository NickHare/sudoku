export function getElementById(id, parent=document){
    return parent.getElementById(id);
}

export function getElementsByClassName(className, parent=document){
    return [ ...parent.getElementsByClassName(className) ];
}

export function createElement(tag, classList=[], childList=[]){
    let element = document.createElement(tag);
    classList.forEach(className => element.classList.add(className));
    childList.forEach(child => element.appendChild(child));
    return element;
}