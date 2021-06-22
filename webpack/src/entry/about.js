// Entry File

import "../css/style.css";
import hello_word from "../js/hello.js";
import world_word from "../js/world.js";

const word = `About ${world_word} ${hello_word}`;
document.querySelector("#about").innerHTML = word;
