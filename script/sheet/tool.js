import { DarkHeresyItemSheet } from "./item.js";

export class ToolSheet extends DarkHeresyItemSheet {
    static get defaultOptions() {
        return mergeObject(super.defaultOptions, {
            classes: ["dark-eye-5", "sheet", "tool"],
            template: "systems/dark-eye-5/template/sheet/tool.html",
            width: 500,
            height: 369,
            resizable: false,
            tabs: [
                {
                    navSelector: ".sheet-tabs",
                    contentSelector: ".sheet-body",
                    initial: "stats",
                },
            ]
        });
    }

    getData() {
        const data = super.getData();
        return data;
    }

    _getHeaderButtons() {
        let buttons = super._getHeaderButtons();
        buttons = [].concat(buttons);
        return buttons;
    }

    activateListeners(html) {
        super.activateListeners(html);
    }
}