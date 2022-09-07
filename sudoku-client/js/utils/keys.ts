export class KeyUtils{
    static arrowKeys: string[] = [ "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight" ];
    static digitKeys: string[] = [ ...Array(9).keys() ].map(index => (index + 1).toString());
    static backspaceKey: string = "Backspace";
    static enterKey: string = "Enter";

    static isArrowKey(event: KeyboardEvent): boolean{
        return KeyUtils.arrowKeys.includes(event.key);
    }
    
    static isDigitKey(event: KeyboardEvent): boolean{
        return KeyUtils.digitKeys.includes(event.key);
    }

    static isBackspaceKey(event: KeyboardEvent): boolean{
        return event.key == KeyUtils.backspaceKey;
    }

    static isEnterKey(event: KeyboardEvent): boolean{
        return event.key == KeyUtils.backspaceKey;
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