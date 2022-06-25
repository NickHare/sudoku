export class DomUtils{

    static getElementById(id, parent=document){
        return parent.getElementById(id);
    }

    static getElementsByClass(className, parent=document){
        return [ ...parent.getElementsByClassName(className) ];
    }

    static hasElementClass(element, className){
        return element.classList.contains(className);
    }

    static getElementClasses(element){
        return [ ...element.classList ];
    }
   
    static setElementClasses(element, classNames){
        element.classList.forEach(className => element.classList.remove(className));
        classNames.forEach(className => element.classList.add(className));
        return element;
    }

    static addElementClass(element, className){
        element.classList.add(className);
        return element;
    }

    static addElementClasses(element, classNames){
        classNames?.forEach(className => element.classList.add(className));
        return element;
    }
    
    static removeElementClass(element, className){
        element?.classList?.remove(className);
        return element;
    }
    
    static removeElementClasses(element, classNames){
        classNames?.forEach(className => element.classList.remove(className));
        return element;
    }

    static removeAllElementClasses(element){
        element?.classList?.forEach(className => element.classList.remove(className));
        return element;
    }

    static getElementDataset(element){
        return element?.dataset;
    }

    static getElemenetDatasetProperty(element, propertyName){
        return element?.dataset?.[propertyName];
    }

    static setElemenetDatasetPropery(element, propertyName, propertyValue){
        if (element?.dataset == null || propertyName == null || propertyValue == null){
            return null;
        }
        

    }
    
    static createElement(tag, classList=[], childList=[]){
        let element = document.createElement(tag);
        classList.forEach(className => element.classList.add(className));
        childList.forEach(child => element.appendChild(child));
        return element;
    }

    static createTextNode(text){
        return document.createTextNode(text);
    }  

    static isTextNode(node){
        return node != null && node.constructor.name == "Text";
    } 

    static hasElementChildNodes(element){
        return element.hasChildNodes();
    }

    static getElementChildNodes(element){
        return [ ...element.childNodes ];
    }

    static addElementChildNode(element, child){
        element.appendChild(child);
        return element;
    }

    static addElementChildNodeBefore(element, childNode, index){
        return element.insertBefore(childNode, element.childNodes[index]);
    }

    static addElementChileNodes(element, childNodes){
        childNodes.forEach(child => element.appendChild(child));
        return element;
    }

    static removeElementChildNode(element, childNode){
        element.removeChild(childNode);
        return element;
    }

    static removeElementChildNodes(element, childNodes){
        childNodes.forEach(child => element.removeChild(child));
        return element;
    }

    static removeAllElementChildNodes(element){
        while (element.hasChildNodes()){
            element.removeChild(element.firstChild);
        }
        return element;
    }
}