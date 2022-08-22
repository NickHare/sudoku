export class KeyUtils{
    static arrowKeys = [ "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight" ];
    static digitKeys = [ ...Array(9).keys() ].map(index => (index + 1).toString());

    static isArrowKey(event: KeyboardEvent): boolean{
        return KeyUtils.arrowKeys.includes(event.key);
    }
    
    static isDigitKey(event: KeyboardEvent): boolean{
        return KeyUtils.digitKeys.includes(event.key);
    }
    
    static isShiftActive(event: KeyboardEvent): boolean{
        return event.shiftKey;
    }
    
    static isCtrlActive(event: KeyboardEvent): boolean{
        return event.ctrlKey;
    }
    
    static isAltActive(event: KeyboardEvent): boolean{
        return event.altKey;
    }
}