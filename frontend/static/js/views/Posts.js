import AbstractView from "./AbstractView.js";
import data from './data.json' assert { type: 'JSON' };

export default class extends AbstractView {
    constructor(params) {
        super(params);
        this.setTitle("Nicolas Gatien");
    }

    async getHtml() {
        return `
            <h1>Nicolas Gatien</h1>
            <p>Top 3 Important Details</p>
        `;
    }
}