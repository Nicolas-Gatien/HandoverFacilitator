import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor(params) {
        super(params);
        this.setTitle("Nicolas Gatien");
    }

    async getHtml() {
        return `
            <h1>Nicolas Gatien</h1>
            <p>Enter Medical Record</p>
            <textarea id="recordText" name="recordText" class="recordText"></textarea>        
            `;
    }
}