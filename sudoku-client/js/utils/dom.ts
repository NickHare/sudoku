export class DomUtils{

    static getElementById(id: string): HTMLElement | null{
        return document.getElementById(id);
    }

    static getElementsByClass(className: string): HTMLElement[]{
        return [ ...document.getElementsByClassName(className) ] as HTMLElement[];
    }

    static hasElementClass(element: HTMLElement, className: string): boolean{
        return element.classList.contains(className);
    }

    static getElementClasses(element: HTMLElement): string[]{
        return [ ...element.classList ];
    }
   
    static setElementClasses(element: HTMLElement, classNames: string[]): HTMLElement{
        element.className = "";
        classNames.forEach(className => element.classList.add(className));
        return element;
    }

    static addElementClass(element: HTMLElement, className: string): HTMLElement{
        element.classList.add(className);
        return element;
    }

    static addElementClasses(element: HTMLElement, classNames: string[]): HTMLElement{
        classNames.forEach(className => element.classList.add(className));
        return element;
    }
    
    static removeElementClass(element: HTMLElement, className: string): HTMLElement{
        element.classList.remove(className);
        return element;
    }
    
    static removeElementClasses(element: HTMLElement, classNames: string[]): HTMLElement{
        classNames.forEach(className => element.classList.remove(className));
        return element;
    }

    static removeAllElementClasses(element: HTMLElement): HTMLElement{
        element?.classList?.forEach(className => element.classList.remove(className));
        return element;
    }

    static getElementAttribute(element: HTMLElement, attributeName: string): string | null{
        return element.getAttribute(attributeName);
    }

    static setElementAttribute(element: HTMLElement, attributeName: string, attributeValue: string): HTMLElement{
        element.setAttribute(attributeName, attributeValue);
        return element;
    }
    
    static removeElementAttribute(element: HTMLElement, attributeName: string): HTMLElement{
        element.removeAttribute(attributeName);
        return element;
    }

    static getElementDataset(element: HTMLElement): DOMStringMap{
        return element.dataset;
    }

    static getElemenetDatasetProperty(element: HTMLElement, propertyName: string): string | undefined{
        return element.dataset[propertyName];
    }

    static setElemenetDatasetPropery(element: HTMLElement, propertyName: string, propertyValue: string): HTMLElement{
        element.dataset[propertyName] = propertyValue;
        return element;
    }
    
    static createElement(tag: string, classList: string[]=[], childList: Node[]=[]): HTMLElement{
        const element = document.createElement(tag);
        classList.forEach(className => element.classList.add(className));
        childList.forEach(child => element.appendChild(child));
        return element;
    }

    static createTextNode(text: string): Node{
        return document.createTextNode(text);
    }  

    static isTextNode(node: Node): boolean{
        return node != null && node.constructor.name == "Text";
    } 

    static hasElementChildNodes(element: HTMLElement): boolean{
        return element.hasChildNodes();
    }

    static getElementChildNodes(element: HTMLElement): Node[]{
        return [ ...element.childNodes ];
    }

    static addElementChildNode(element: HTMLElement, child: Node): HTMLElement{
        element.appendChild(child);
        return element;
    }

    static addElementChildNodes(element: HTMLElement, childNodes: Node[]): HTMLElement{
        childNodes.forEach(child => element.appendChild(child));
        return element;
    }

    static removeElementChildNode(element: HTMLElement, childNode: Node): HTMLElement{
        element.removeChild(childNode);
        return element;
    }

    static removeElementChildNodes(element: HTMLElement, childNodes: Node[]): HTMLElement{
        childNodes.forEach(child => element.removeChild(child));
        return element;
    }

    static removeAllElementChildNodes(element: HTMLElement): HTMLElement{
        while (element.firstChild != null && element.firstChild != undefined){
            element.removeChild(element.firstChild);
        }
        return element;
    }

    static focusElement(element: HTMLElement): HTMLElement{
        element.focus();
        return element;
    }
}