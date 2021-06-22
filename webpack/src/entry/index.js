// Entry File

import "../css/style.css";
import hello_word from "../js/hello.js";
import world_word from "../js/world.js";

const word = `${hello_word} ${world_word}`;
document.querySelector("#root").innerHTML = word;
